import pytest

from app.fps import FPSCounter


def make_clock(times):
    iterator = iter(times)
    return lambda: next(iterator)


def test_first_tick_has_no_fps():
    counter = FPSCounter(clock=make_clock([0.0]))

    assert counter.tick() == 0.0


def test_steady_rate():
    counter = FPSCounter(clock=make_clock([0.0, 0.1, 0.2, 0.3]))

    values = [counter.tick() for _ in range(4)]

    assert values[-1] == pytest.approx(10.0)


@pytest.mark.parametrize("smoothing", [-0.1, 1.0])
def test_invalid_smoothing_is_rejected(smoothing):
    with pytest.raises(ValueError):
        FPSCounter(smoothing=smoothing)
