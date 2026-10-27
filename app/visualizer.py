import cv2
from ultralytics.engine.results import Results


class Visualizer:
    """Display object detection results."""

    def __init__(self, window_name: str = "Real-Time Object Detection") -> None:
        self.window_name = window_name

    def show(self, result: Results) -> bool:
        """Display an annotated frame.

        Return False when the user requests to quit.
        """
        frame = result.plot()
        cv2.imshow(self.window_name, frame)

        return (cv2.waitKey(1) & 0xFF) != ord("q")

    def close(self) -> None:
        """Close all OpenCV windows."""
        cv2.destroyAllWindows()
