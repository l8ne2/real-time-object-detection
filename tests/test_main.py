from types import SimpleNamespace
from unittest.mock import MagicMock

import numpy as np
import pytest

from app import main as main_module
from app.main import main, run_image, run_stream
from app.stats import DetectionStats


@pytest.fixture
def result():
    return SimpleNamespace(
        names={0: "person"},
        boxes=SimpleNamespace(cls=np.array([0])),
    )


@pytest.fixture
def detector(result):
    mock = MagicMock()
    mock.detect.return_value = result
    return mock


@pytest.fixture
def visualizer():
    mock = MagicMock()
    mock.show.return_value = True
    return mock


@pytest.fixture
def make_camera(monkeypatch):
    """Build a fake Camera that returns the given frames in order."""

    def _make(frames, opens=True, live=False):
        camera = MagicMock()
        camera.open.return_value = opens
        camera.read.side_effect = frames
        camera.is_live = live
        monkeypatch.setattr(main_module, "Camera", MagicMock(return_value=camera))
        return camera

    return _make


# --- run_stream -------------------------------------------------------------


def test_stream_processes_a_video_until_the_end(
    make_camera, detector, visualizer, frame
):
    camera = make_camera([frame, frame, None])
    stats = DetectionStats()

    code = run_stream("video.mp4", detector, visualizer, stats)

    assert code == 0
    assert stats.frames == 2
    assert stats.counts["person"] == 2
    camera.release.assert_called_once()


def test_stream_fails_when_the_source_cannot_be_opened(
    make_camera, detector, visualizer
):
    make_camera([], opens=False)

    code = run_stream(0, detector, visualizer, DetectionStats())

    assert code == 1
    detector.detect.assert_not_called()


def test_stream_fails_when_a_live_camera_stops_responding(
    make_camera, detector, visualizer
):
    camera = make_camera([None], live=True)

    code = run_stream(0, detector, visualizer, DetectionStats())

    assert code == 1
    camera.release.assert_called_once()


def test_stream_stops_when_the_user_quits(make_camera, detector, visualizer, frame):
    make_camera([frame, frame, frame])
    visualizer.show.return_value = False
    stats = DetectionStats()

    code = run_stream(0, detector, visualizer, stats)

    assert code == 0
    assert stats.frames == 1


def test_stream_handles_keyboard_interrupt(make_camera, detector, visualizer, frame):
    camera = make_camera([frame])
    detector.detect.side_effect = KeyboardInterrupt

    code = run_stream(0, detector, visualizer, DetectionStats())

    assert code == 0
    camera.release.assert_called_once()


# --- run_image --------------------------------------------------------------


def test_image_is_detected_and_shown(monkeypatch, detector, visualizer, frame, result):
    monkeypatch.setattr(main_module.cv2, "imread", lambda path: frame)
    stats = DetectionStats()

    code = run_image("photo.jpg", detector, visualizer, stats)

    assert code == 0
    assert stats.counts["person"] == 1
    visualizer.show.assert_called_once_with(result, wait=True)


def test_unreadable_image_returns_an_error(monkeypatch, detector, visualizer):
    monkeypatch.setattr(main_module.cv2, "imread", lambda path: None)

    code = run_image("missing.jpg", detector, visualizer, DetectionStats())

    assert code == 1
    detector.detect.assert_not_called()


# --- main -------------------------------------------------------------------


@pytest.fixture
def patched_main(monkeypatch):
    """Replace everything main() builds or runs."""
    visualizer_class = MagicMock()
    mocks = SimpleNamespace(
        run_image=MagicMock(return_value=0),
        run_stream=MagicMock(return_value=0),
        visualizer=visualizer_class.return_value,
    )
    monkeypatch.setattr(main_module, "ObjectDetector", MagicMock())
    monkeypatch.setattr(main_module, "Visualizer", visualizer_class)
    monkeypatch.setattr(main_module, "run_image", mocks.run_image)
    monkeypatch.setattr(main_module, "run_stream", mocks.run_stream)
    return mocks


def test_main_runs_image_mode_for_an_image_source(patched_main):
    assert main(["--source", "photo.jpg"]) == 0

    patched_main.run_image.assert_called_once()
    patched_main.run_stream.assert_not_called()
    patched_main.visualizer.close.assert_called_once()


def test_main_runs_stream_mode_by_default(patched_main):
    assert main([]) == 0

    patched_main.run_stream.assert_called_once()
    patched_main.run_image.assert_not_called()


def test_main_returns_the_exit_code_of_the_run(patched_main):
    patched_main.run_stream.return_value = 1

    assert main([]) == 1


def test_main_closes_the_windows_even_on_error(patched_main):
    patched_main.run_stream.side_effect = RuntimeError("boom")

    with pytest.raises(RuntimeError):
        main([])

    patched_main.visualizer.close.assert_called_once()
