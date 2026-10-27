import pytest

from app.config import Config


@pytest.mark.parametrize("source", ["photo.jpg", "PHOTO.PNG", "dir/img.webp"])
def test_image_sources(source):
    assert Config(source=source).is_image


@pytest.mark.parametrize("source", [0, "video.mp4"])
def test_non_image_sources(source):
    assert not Config(source=source).is_image