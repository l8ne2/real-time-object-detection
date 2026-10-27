from types import SimpleNamespace

import numpy as np
import pytest

from app.detector import ObjectDetector, extract_labels


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
def test_extract_labels_returns_class_names():
    result = SimpleNamespace(
        names={0: "person", 1: "car"},
        boxes=SimpleNamespace(cls=np.array([0, 0, 1])),
    )

    assert extract_labels(result) == ["person", "person", "car"]


def test_extract_labels_without_boxes():
    result = SimpleNamespace(names={}, boxes=None)

    assert extract_labels(result) == []