from dataclasses import dataclass
from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


@dataclass(frozen=True)
class Config:
    """Application settings, built from the command line."""

    model: str = "yolov8n.pt"
    confidence: float = 0.5
    source: int | str = 0
    verbose: bool = False

    @property
    def is_image(self) -> bool:
        """True when the source is a path to an image file."""
        return (
            isinstance(self.source, str)
            and Path(self.source).suffix.lower() in IMAGE_EXTENSIONS
        )
