import logging

import cv2
import numpy as np

logger = logging.getLogger(__name__)


class Camera:
    """Manage webcam capture."""

    def __init__(self, camera_index: int = 0) -> None:
        self.camera_index = camera_index
        self.capture: cv2.VideoCapture | None = None

    def open(self) -> bool:
        """Open the selected camera. Return True on success."""
        self.capture = cv2.VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            logger.error("Cannot open camera %d", self.camera_index)
            self.capture.release()
            self.capture = None
            return False

        logger.info("Camera %d opened", self.camera_index)
        return True

    def read(self) -> np.ndarray | None:
        """Capture one frame, or return None if the capture failed."""
        if self.capture is None or not self.capture.isOpened():
            raise RuntimeError("Camera is not open.")

        success, frame = self.capture.read()

        if not success:
            return None

        return frame

    def release(self) -> None:
        """Release the camera resource."""
        if self.capture is not None:
            self.capture.release()
            self.capture = None
            logger.info("Camera released")
