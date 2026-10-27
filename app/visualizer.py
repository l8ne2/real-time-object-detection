import cv2
import numpy as np
from ultralytics.engine.results import Results


class Visualizer:
    """Display object detection results."""

    def __init__(self, window_name: str = "Real-Time Object Detection") -> None:
        self.window_name = window_name

    def show(
        self,
        result: Results,
        fps: float | None = None,
        wait: bool = False,
    ) -> bool:
        """Display an annotated frame.

        Wait for a key press when `wait` is True (single image).
        Return False when the user requests to quit.
        """
        frame = result.plot()

        if fps is not None:
            self._draw_text(frame, f"FPS: {fps:.1f}", (10, 30))
        self._draw_text(frame, f"Objects: {len(result.boxes)}", (10, 60))

        cv2.imshow(self.window_name, frame)
        key = cv2.waitKey(0 if wait else 1) & 0xFF

        return key != ord("q")

    @staticmethod
    def _draw_text(frame: np.ndarray, text: str, origin: tuple[int, int]) -> None:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, origin, font, 0.8, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(frame, text, origin, font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

    def close(self) -> None:
        """Close all OpenCV windows."""
        cv2.destroyAllWindows()