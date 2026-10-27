import logging

import cv2

from app.camera import Camera
from app.cli import parse_args
from app.detector import ObjectDetector, extract_labels
from app.fps import FPSCounter
from app.stats import DetectionStats
from app.visualizer import Visualizer

logger = logging.getLogger(__name__)


def run_image(
    path: str,
    detector: ObjectDetector,
    visualizer: Visualizer,
    stats: DetectionStats,
) -> int:
    """Detect objects in a single image. Return an exit code."""
    frame = cv2.imread(path)

    if frame is None:
        logger.error("Cannot read image %s", path)
        return 1

    result = detector.detect(frame)
    stats.update(extract_labels(result))
    visualizer.show(result, wait=True)
    return 0


def run_stream(
    source: int | str,
    detector: ObjectDetector,
    visualizer: Visualizer,
    stats: DetectionStats,
) -> int:
    """Detect objects in a webcam or video stream. Return an exit code."""
    camera = Camera(source)

    if not camera.open():
        return 1

    fps_counter = FPSCounter()

    try:
        while True:
            frame = camera.read()

            if frame is None:
                if camera.is_live:
                    logger.error("Could not read a frame from the camera")
                    return 1
                logger.info("End of video")
                break

            result = detector.detect(frame)
            stats.update(extract_labels(result))

            if not visualizer.show(result, fps=fps_counter.tick()):
                break

    except KeyboardInterrupt:
        logger.info("Stopped by user")

    finally:
        camera.release()

    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the application. Return a process exit code."""
    config = parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if config.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    detector = ObjectDetector(config.model, config.confidence)
    visualizer = Visualizer()
    stats = DetectionStats()

    try:
        if config.is_image:
            code = run_image(config.source, detector, visualizer, stats)
        else:
            code = run_stream(config.source, detector, visualizer, stats)
    finally:
        visualizer.close()

    if stats.frames:
        logger.info("Session summary:\n%s", stats.summary())

    return code


if __name__ == "__main__":
    raise SystemExit(main())
