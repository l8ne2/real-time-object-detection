import numpy as np
import pytest

from app.detector import ObjectDetector


def test_detector_rejects_invalid_confidence():
    with pytest.raises(ValueError):
        ObjectDetector.__new__(ObjectDetector).__init__(
            model_path="unused.pt",
            confidence=1.5,
        )


def test_detector_rejects_negative_confidence():
    with pytest.raises(ValueError):
        ObjectDetector.__new__(ObjectDetector).__init__(
            model_path="unused.pt",
            confidence=-0.1,
        )


def test_detector_rejects_empty_image():
    detector = ObjectDetector.__new__(ObjectDetector)
    detector.confidence = 0.5
    detector.model = None

    empty_frame = np.array([])

    with pytest.raises(ValueError, match="must not be empty"):
        detector.detect(empty_frame)
