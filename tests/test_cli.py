import pytest

from app.cli import parse_args
from app.config import Config


def test_defaults():
    assert parse_args([]) == Config()


def test_custom_values():
    config = parse_args(
        ["--model", "yolov8s.pt", "--conf", "0.7", "--source", "video.mp4", "-v"]
    )

    assert config == Config(
        model="yolov8s.pt",
        confidence=0.7,
        source="video.mp4",
        verbose=True,
    )


def test_numeric_source_is_a_camera_index():
    assert parse_args(["--source", "1"]).source == 1


@pytest.mark.parametrize("value", ["1.5", "-0.1", "abc"])
def test_invalid_confidence_is_rejected(value):
    with pytest.raises(SystemExit):
        parse_args([f"--conf={value}"])
