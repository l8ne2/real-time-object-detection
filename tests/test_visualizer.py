from types import SimpleNamespace
from unittest.mock import MagicMock

import numpy as np
import pytest

from app import visualizer as visualizer_module
from app.visualizer import Visualizer


@pytest.fixture
def cv2_mocks(monkeypatch):
    """Replace the OpenCV window functions."""
    mocks = SimpleNamespace(
        imshow=MagicMock(),
        waitKey=MagicMock(return_value=-1),
        destroyAllWindows=MagicMock(),
    )
    for name in ("imshow", "waitKey", "destroyAllWindows"):
        monkeypatch.setattr(visualizer_module.cv2, name, getattr(mocks, name))
    return mocks


@pytest.fixture
def result():
    return SimpleNamespace(
        plot=lambda: np.zeros((50, 200, 3), dtype=np.uint8),
        boxes=[object(), object()],
    )


def test_show_displays_the_frame(cv2_mocks, result):
    visualizer = Visualizer("My window")

    assert visualizer.show(result, fps=30.0) is True
    assert cv2_mocks.imshow.call_args.args[0] == "My window"


def test_show_returns_false_when_q_is_pressed(cv2_mocks, result):
    cv2_mocks.waitKey.return_value = ord("q")

    assert Visualizer().show(result) is False


def test_show_does_not_block_by_default(cv2_mocks, result):
    Visualizer().show(result)

    cv2_mocks.waitKey.assert_called_once_with(1)


def test_show_waits_for_a_key_in_wait_mode(cv2_mocks, result):
    Visualizer().show(result, wait=True)

    cv2_mocks.waitKey.assert_called_once_with(0)


def test_close_destroys_all_windows(cv2_mocks):
    Visualizer().close()

    cv2_mocks.destroyAllWindows.assert_called_once()
