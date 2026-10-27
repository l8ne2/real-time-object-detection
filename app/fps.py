import time
from collections.abc import Callable


class FPSCounter:
    """Measure a smoothed frames-per-second rate."""

    def __init__(
        self,
        smoothing: float = 0.9,
        clock: Callable[[], float] = time.perf_counter,
    ) -> None:
        if not 0.0 <= smoothing < 1.0:
            raise ValueError("Smoothing must be in [0, 1).")

        self.smoothing = smoothing
        self.fps = 0.0
        self._clock = clock
        self._last: float | None = None

    def tick(self) -> float:
        """Register a new frame and return the current FPS."""
        now = self._clock()

        if self._last is not None:
            elapsed = now - self._last
            if elapsed > 0:
                instant = 1.0 / elapsed
                if self.fps == 0.0:
                    self.fps = instant
                else:
                    self.fps = (
                        self.smoothing * self.fps + (1 - self.smoothing) * instant
                    )

        self._last = now
        return self.fps