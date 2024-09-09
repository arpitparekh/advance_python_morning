import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
drawing_utils = mp_drawing.DrawingSpec(thickness=2, circle_radius=2)

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# To store previous hand positions for gesture detection
prev_positions = []
max_positions = 10

def detect_waving(positions):
    if len(positions) < max_positions:
        return False

    # Calculate the distance between the first and the last position
    dist = np.linalg.norm(np.array(positions[0]) - np.array(positions[-1]))
    return dist > 0.05  # Adjust the threshold as needed

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks and gestures
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, drawing_utils, drawing_utils)

            # Get the position of the wrist
            landmarks = hand_landmarks.landmark
            wrist = landmarks[mp_hands.HandLandmark.WRIST]
            position = (wrist.x, wrist.y)

            # Store positions and detect waving gesture
            prev_positions.append(position)
            if len(prev_positions) > max_positions:
                prev_positions.pop(0)

            if detect_waving(prev_positions):
                print("Waving detected! Closing application.")
                cap.release()
                cv2.destroyAllWindows()
                exit()

    # Display the resulting frame
    cv2.imshow('Hand Gesture Detector', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
