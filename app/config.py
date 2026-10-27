from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """Application settings, built from the command line."""

    model: str = "yolov8n.pt"
    confidence: float = 0.5
    source: int | str = 0
    verbose: bool = False
