from ultralytics import YOLO


class ObjectDetector:
    """Detect objects in images using a pretrained YOLO model."""

    def __init__(
        self,
        model_path: str = "yolov8n.pt",
        confidence: float = 0.5,
    ) -> None:
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")

        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame):
        """Return detection results for an image."""
        if frame is None or frame.size == 0:
            raise ValueError("The input image must not be empty.")

        result = self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False,
        )[0]

        return result