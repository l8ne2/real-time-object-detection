import numpy as np
import pytest


@pytest.fixture
def frame() -> np.ndarray:
    """A small black image, usable as a fake camera frame."""
    return np.zeros((48, 64, 3), dtype=np.uint8)
