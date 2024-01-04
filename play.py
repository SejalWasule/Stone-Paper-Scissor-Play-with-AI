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
    
    # Get user's move (you can implement a way to detect the user's gesture)
    user_move = "rock"  # Replace with the actual user's move
    
    # Determine the winner
    if user_move == predicted_class:
        result = "It's a tie!"
    elif (user_move == "rock" and predicted_class == "scissors") or \
         (user_move == "scissors" and predicted_class == "paper") or \
         (user_move == "paper" and predicted_class == "rock"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Display the predicted class and result with a slightly smaller font (scale 0.35)
    cv2.putText(frame, "Your Move: " + user_move, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.putText(frame, "Computer's Move: " + predicted_class, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.putText(frame, "Result: " + result, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)  # Adjust the scale (0.35) for a slightly smaller font
    
    # Display the frame
    cv2.imshow('Live Detection', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
