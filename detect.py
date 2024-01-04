import cv2
import numpy as np
import tensorflow as tf

# Load the trained model from the H5 file
model = tf.keras.models.load_model('newrps_cnn.h5')

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, adjust if needed

# Define a list of class labels
class_labels = ["rock", "paper", "scissors"]

# Set the window size
cv2.namedWindow('Live Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Live Detection', 800, 600)  # Adjust the width and height as needed

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    
    # Preprocess the frame to match the model's input shape
    frame = cv2.resize(frame, (150, 150))  # Resize the frame to (150, 150)
    frame = frame / 255.0  # Normalize pixel values to the range [0, 1]
    
    # Perform inference using your loaded model
    # Make sure the frame is in the correct format (e.g., NumPy array)
    prediction = model.predict(np.expand_dims(frame, axis=0))
    
    # Get the class label with the highest probability
    predicted_class = class_labels[prediction.argmax()]
    
    # Display the predicted class on the frame with a smaller font
    cv2.putText(frame, "Prediction: " + predicted_class, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    # Display the frame
    cv2.imshow('Live Detection', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
