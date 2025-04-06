import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import time
from utils.shape_predictor.sounds.play_sounds import start_alarm, stop_alarm
# Load face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"D:\RANJEET\sap\car_dash\pro1234\utils\shape_predictor\shape_predictor_68_face_landmarks_GTX.dat")  # Ensure the model file is in the same directory

# Function to compute Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Define eye landmarks (from dlib's 68 facial landmarks)
LEFT_EYE_LANDMARKS = list(range(36, 42))
RIGHT_EYE_LANDMARKS = list(range(42, 48))

# Eye closure threshold
EYE_CLOSED_THRESHOLD = 0.25
EYE_CLOSED_FRAMES = 2  # Number of frames eyes must be closed to trigger warning

counter = 0  # Closed-eye frame counter

def main(ret, frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = detector(gray)  # Detect faces
    global counter
    for face in faces:
        landmarks = predictor(gray, face)  # Get facial landmarks
        
        # Extract eye coordinates
        left_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in LEFT_EYE_LANDMARKS]
        right_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in RIGHT_EYE_LANDMARKS]

        # Compute EAR for both eyes
        left_EAR = eye_aspect_ratio(left_eye)
        right_EAR = eye_aspect_ratio(right_eye)
        avg_EAR = (left_EAR + right_EAR) / 2.0

        # Draw eyes
        for (x, y) in left_eye + right_eye:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # Drowsiness detection logic
        if avg_EAR < EYE_CLOSED_THRESHOLD:
            counter += 1
            if counter >= EYE_CLOSED_FRAMES:
                cv2.putText(frame, "DROWSY! WAKE UP!", (100, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("*"*50,"/nDrowsiness detected!")
                start_alarm()

                
                
        else:
            counter = 0  # Reset counter if eyes are open
    # cv2.imshow("Driver State Monitoring", frame)  # Display video feed
    if counter == 0:
        stop_alarm()  # Stop alarm if eyes are open
    


    
    
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # Start webcam

    while True:
        
        ret, frame = cap.read()
        if not ret:
            break
        
        main(ret, frame)
        
        cv2.imshow("Driver State Monitoring", frame)  # Display video feed

        if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
