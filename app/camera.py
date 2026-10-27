import logging

import cv2
import numpy as np

logger = logging.getLogger(__name__)


class Camera:
    """Read frames from a webcam or a video file."""

    def __init__(self, source: int | str = 0) -> None:
        self.source = source
        self.capture: cv2.VideoCapture | None = None

    @property
    def is_live(self) -> bool:
        """True for a webcam, False for a video file."""
        return isinstance(self.source, int)

    def open(self) -> bool:
        """Open the selected source. Return True on success."""
        self.capture = cv2.VideoCapture(self.source)

        if not self.capture.isOpened():
            logger.error("Cannot open source %s", self.source)
            self.capture.release()
            self.capture = None
            return False

        logger.info("Source %s opened", self.source)
        return True

    def read(self) -> np.ndarray | None:
        """Capture one frame, or return None if nothing could be read."""
        if self.capture is None or not self.capture.isOpened():
            raise RuntimeError("Camera is not open.")

        success, frame = self.capture.read()

        if not success:
            return None

        return frame

    def release(self) -> None:
        """Release the capture resource."""
        if self.capture is not None:
            self.capture.release()
            self.capture = None
            logger.info("Source released")
