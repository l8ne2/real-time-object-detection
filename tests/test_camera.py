from unittest.mock import MagicMock

import pytest

from app import camera as camera_module
from app.camera import Camera


@pytest.fixture
def fake_capture(monkeypatch, frame):
    """Replace cv2.VideoCapture with a controllable fake."""
    capture = MagicMock()
    capture.isOpened.return_value = True
    capture.read.return_value = (True, frame)
    monkeypatch.setattr(
        camera_module.cv2,
        "VideoCapture",
        MagicMock(return_value=capture),
    )
    return capture


def test_open_succeeds(fake_capture):
    camera = Camera(0)

    assert camera.open() is True
    assert camera.capture is fake_capture


def test_open_failure_releases_the_capture(fake_capture):
    fake_capture.isOpened.return_value = False
    camera = Camera(5)

    assert camera.open() is False
    assert camera.capture is None
    fake_capture.release.assert_called_once()


def test_read_before_open_raises():
    with pytest.raises(RuntimeError, match="not open"):
        Camera().read()


def test_read_returns_the_frame(fake_capture, frame):
    camera = Camera()
    camera.open()

    assert camera.read() is frame


def test_read_returns_none_when_capture_fails(fake_capture):
    fake_capture.read.return_value = (False, None)
    camera = Camera()
    camera.open()

    assert camera.read() is None


def test_release_is_idempotent(fake_capture):
    camera = Camera()
    camera.open()

    camera.release()
    camera.release()

    fake_capture.release.assert_called_once()
    assert camera.capture is None


@pytest.mark.parametrize(
    ("source", "expected"),
    [(0, True), (2, True), ("video.mp4", False)],
)
def test_is_live(source, expected):
    assert Camera(source).is_live is expected
