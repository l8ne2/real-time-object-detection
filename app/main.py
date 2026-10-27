import logging

from app.camera import Camera
from app.detector import ObjectDetector
from app.visualizer import Visualizer

logger = logging.getLogger(__name__)


def main() -> int:
    """Run the detection loop. Return a process exit code."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    camera = Camera()
    detector = ObjectDetector()
    visualizer = Visualizer()

    if not camera.open():
        return 1

    try:
        while True:
            frame = camera.read()

            if frame is None:
                logger.error("Could not read a frame from the camera")
                return 1

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
