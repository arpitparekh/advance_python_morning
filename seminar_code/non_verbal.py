import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and DrawingUtils
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Define function to get finger states
def get_finger_status(landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_bases = [2, 6, 10, 14, 18]
    finger_states = []
    for tip, base in zip(finger_tips, finger_bases):
        if landmarks[tip].y < landmarks[base].y:
            finger_states.append('Up')
        else:
            finger_states.append('Down')
    return finger_states

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            finger_states = get_finger_status(hand_landmarks.landmark)
            print(finger_states)  # Print finger states to the console for now

    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
