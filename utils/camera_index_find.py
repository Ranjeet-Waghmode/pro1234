import cv2

def find_camera_index():
    print("Searching for available cameras...")

    # Try camera indices from 0 to 10
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cap.release()
            print(f"Camera found at index: {i}")
            return i
        else:
            print(f"No camera found at index: {i}")

    print("No camera found.")
    return None

index = find_camera_index()

if index is not None:
    cap = cv2.VideoCapture(index)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading the frame")
            break

        cv2.imshow("Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    print("No camera available.")