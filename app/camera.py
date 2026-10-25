import cv2


class Camera:
    """Manage webcam capture."""

    def __init__(self, camera_index: int = 0) -> None:
        self.camera_index = camera_index
        self.capture = None

    def open(self) -> bool:
        """Open the selected camera."""
        self.capture = cv2.VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            self.capture.release()
            self.capture = None
            return False

        return True

    def read(self):
        """Capture one frame from the camera."""
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