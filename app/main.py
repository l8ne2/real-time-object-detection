import logging

from app.camera import Camera
from app.cli import parse_args
from app.detector import ObjectDetector
from app.visualizer import Visualizer

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    """Run the detection loop. Return a process exit code."""
    config = parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if config.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    camera = Camera(config.source)
    detector = ObjectDetector(config.model, config.confidence)
    visualizer = Visualizer()

    if not camera.open():
        return 1

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

            if not visualizer.show(result):
                break

    except KeyboardInterrupt:
        logger.info("Stopped by user")

    finally:
        camera.release()
        visualizer.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
