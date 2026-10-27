from types import SimpleNamespace
from unittest.mock import MagicMock

import numpy as np
import pytest

from app import detector as detector_module
from app.detector import ObjectDetector, extract_labels


@pytest.fixture
def fake_yolo(monkeypatch):
    """Replace the YOLO class so that no real model is loaded."""
    model = MagicMock()
    model.predict.return_value = ["first-result"]
    factory = MagicMock(return_value=model)
    monkeypatch.setattr(detector_module, "YOLO", factory)
    return SimpleNamespace(factory=factory, model=model)


@pytest.mark.parametrize("confidence", [1.5, -0.1])
def test_invalid_confidence_is_rejected(fake_yolo, confidence):
    with pytest.raises(ValueError, match="between 0 and 1"):
        ObjectDetector(confidence=confidence)

    fake_yolo.factory.assert_not_called()


def test_model_is_loaded_from_the_given_path(fake_yolo):
    ObjectDetector(model_path="custom.pt")

    fake_yolo.factory.assert_called_once_with("custom.pt")


def test_detect_returns_the_first_result(fake_yolo, frame):
    detector = ObjectDetector(confidence=0.3)

    assert detector.detect(frame) == "first-result"
    fake_yolo.model.predict.assert_called_once_with(
        source=frame,
        conf=0.3,
        verbose=False,
    )


@pytest.mark.parametrize("bad_frame", [None, np.array([])])
def test_detect_rejects_empty_images(fake_yolo, bad_frame):
    detector = ObjectDetector()

    with pytest.raises(ValueError, match="must not be empty"):
        detector.detect(bad_frame)


def test_extract_labels_returns_class_names():
    result = SimpleNamespace(
        names={0: "person", 1: "car"},
        boxes=SimpleNamespace(cls=np.array([0, 0, 1])),
    )

    assert extract_labels(result) == ["person", "person", "car"]


def test_extract_labels_without_boxes():
    result = SimpleNamespace(names={}, boxes=None)

    assert extract_labels(result) == []
