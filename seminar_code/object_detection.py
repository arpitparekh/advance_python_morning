import cv2
import numpy as np

# Load YOLO
cfg_path = "/home/arpit-parekh/bascom_projects/advance_python_morning/seminar_code/yolov3.cfg"
weights_path = "/home/arpit-parekh/bascom_projects/advance_python_morning/seminar_code/yolov3.weights"
names_path = "/home/arpit-parekh/bascom_projects/advance_python_morning/seminar_code/coco.names"

# Load YOLO network
net = cv2.dnn.readNet(weights_path, cfg_path)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load class names
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Get frame dimensions
    height, width, channels = frame.shape

    # Prepare the frame for YOLO model
    blob = cv2.dnn.blobFromImage(frame, scalefactor=0.00392, size=(416, 416),
                               swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Initialize lists for detected objects
    class_ids = []
    confidences = []
    boxes = []

    # Process detections
    for out in outs:
        for detection in out:
            # Each detection is a list of detected objects
            for obj in detection:
                # Convert the obj to a numpy array for better handling
                obj = np.array(obj)
                if obj.ndim == 1:  # Check if obj is a 1D array
                    # Extract scores
                    scores = obj[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        # Object detected
                        center_x = int(obj[0] * width)
                        center_y = int(obj[1] * height)
                        w = int(obj[2] * width)
                        h = int(obj[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

    # Apply Non-Maximum Suppression to remove redundant boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw bounding boxes and labels
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} ({confidence:.2f})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Display the resulting frame
    cv2.imshow('Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
