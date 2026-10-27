import argparse
from importlib.metadata import PackageNotFoundError, version

from app.config import Config


def _get_version() -> str:
    try:
        return version("real-time-object-detection")
    except PackageNotFoundError:
        return "unknown"


def _confidence(value: str) -> float:
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid number: {value!r}") from None

    if not 0.0 <= number <= 1.0:
        raise argparse.ArgumentTypeError("must be between 0 and 1")

    return number


def _source(value: str) -> int | str:
    """A digit-only value is a camera index, anything else is a file path."""
    return int(value) if value.isdigit() else value


def build_parser() -> argparse.ArgumentParser:
    defaults = Config()
    parser = argparse.ArgumentParser(
        prog="object-detect",
        description="Real-time object detection with OpenCV and YOLO.",
    )
    parser.add_argument(
        "--model",
        default=defaults.model,
        help="YOLO model name or path (default: %(default)s)",
    )
    parser.add_argument(
        "--conf",
        dest="confidence",
        type=_confidence,
        default=defaults.confidence,
        help="confidence threshold between 0 and 1 (default: %(default)s)",
    )
    parser.add_argument(
        "--source",
        type=_source,
        default=defaults.source,
        help="camera index or video file path (default: %(default)s)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable debug logging",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {_get_version()}",
    )
    return parser


def parse_args(argv: list[str] | None = None) -> Config:
    args = build_parser().parse_args(argv)
    return Config(
        model=args.model,
        confidence=args.confidence,
        source=args.source,
        verbose=args.verbose,
    )
