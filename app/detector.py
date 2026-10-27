import logging

import numpy as np
from ultralytics import YOLO
from ultralytics.engine.results import Results

logger = logging.getLogger(__name__)


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
        logger.info("Model %s loaded (confidence=%.2f)", model_path, confidence)

    def detect(self, frame: np.ndarray) -> Results:
        """Return detection results for an image."""
        if frame is None or frame.size == 0:
            raise ValueError("The input image must not be empty.")

        return self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False,
        )[0]
def extract_labels(result: Results) -> list[str]:
    """Return the class name of every detection in a result."""
    if result.boxes is None:
        return []

    return [result.names[int(cls)] for cls in result.boxes.cls.tolist()]    
    
