import cv2
import numpy as np
import os

# Paths to the YOLOv3 configuration and weights files
cfg_file_path = r"C:\Users\user\Desktop\CodeAlpha\ARTIFICIAL INTELLIGENCE\Object_Detection\yolov3.cfg"
weights_file_path = r"C:\Users\user\Desktop\CodeAlpha\ARTIFICIAL INTELLIGENCE\Object_Detection\yolov3.weights"
names_file_path = r"C:\Users\user\Desktop\CodeAlpha\ARTIFICIAL INTELLIGENCE\Object_Detection\coco.names"

# Check if files exist
if not os.path.exists(cfg_file_path):
    raise FileNotFoundError(f"Config file not found: {cfg_file_path}")
if not os.path.exists(weights_file_path):
    raise FileNotFoundError(f"Weights file not found: {weights_file_path}")
if not os.path.exists(names_file_path):
    raise FileNotFoundError(f"Names file not found: {names_file_path}")

# Load class names
with open(names_file_path, 'r') as f:
    class_names = [line.strip() for line in f.readlines()]

# Load YOLOv3 network
net = cv2.dnn.readNetFromDarknet(cfg_file_path, weights_file_path)

# Get output layer names
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

# Function to perform object detection
def detect_objects(frame):
    height, width = frame.shape[:2]

    # Preprocess input image
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)

    # Set the input to the network
    net.setInput(blob)

    # Run forward pass to get output of the output layers
    outputs = net.forward(output_layers)

    # Process detections
    detections = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Calculate bounding box coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                detections.append({
                    'box_points': [x, y, x + w, y + h],
                    'name': class_names[class_id],  # Use class names for labels
                    'percentage_probability': confidence * 100
                })

    return detections

# Example usage
cap = cv2.VideoCapture(0)  # Use webcam, change 0 to video file path for video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect_objects(frame)

    for detection in detections:
        box = detection['box_points']
        label = detection['name']
        score = detection['percentage_probability']

        # Draw bounding box
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        # Add label and score
        cv2.putText(frame, f"{label}: {score:.2f}%", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
