import cv2

from app.detector import ObjectDetector


def main():
    detector = ObjectDetector()
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Erreur : impossible d'ouvrir la webcam.")
        return

    try:
        while True:
            success, frame = camera.read()

            if not success:
                print("Erreur : impossible de lire l'image.")
                break

            result = detector.detect(frame)
            annotated_frame = result.plot()

            cv2.imshow("Real-Time Object Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()