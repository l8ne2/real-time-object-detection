from app.camera import Camera
from app.detector import ObjectDetector
from app.visualizer import Visualizer


def main():
    camera = Camera()
    detector = ObjectDetector()
    visualizer = Visualizer()

    if not camera.open():
        print("Erreur : impossible d'ouvrir la webcam.")
        return

    try:
        while True:
            frame = camera.read()

            if frame is None:
                print("Impossible de capturer l'image.")
                break

            result = detector.detect(frame)

            if not visualizer.show(result):
                break

    except KeyboardInterrupt:
        print("\nArrêt demandé.")

    finally:
        camera.release()
        visualizer.close()


if __name__ == "__main__":
    main()