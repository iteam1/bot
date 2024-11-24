import cv2

# Open the webcam (0 is the default camera, use 1 or 2 for other cameras)
cap = cv2.VideoCapture(0)

# # Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame was not successfully captured, break the loop
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Show the captured frame in a window named 'Webcam Feed'
    cv2.imshow('Webcam Feed', frame)

    # Wait for the user to press 'q' to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close the window
cap.release()
cv2.destroyAllWindows()
