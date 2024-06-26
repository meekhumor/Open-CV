import cv2
import numpy as np

def detect_rectangle(image):
    # Get image dimensions
    height, width = image.shape
    
    # Define a threshold for detecting rectangles
    background = 200 
    
    # Initialize variables to store the top-left and bottom-right corner coordinates of the rectangle
    top_left = None
    tli=-1
    tlj=-1
    bri=-1
    brj=-1
    bottom_right=None
    bottom_left=None
    top_right=None
    
    # Iterate through each pixel in the image
    for y in range(height):
        for x in range(width):
            # Check if the pixel intensity is above the threshold
            if image[y, x] <background:
                # If top_left is not set, set it to the current coordinates
                if top_left is None:
                    top_left = (x, y)
                    tli=x
                    tlj=y 
                else:
                    bottom_right=(x,y)
                    bri=x
                    brj=y

    for y in range(height):
        for x in range(width):
           if image[y, x] <background:
               if y<=tlj:
                  bottom_left=(x,y)
               if y>=brj:
                   top_right=(x,y)
    print(top_left,top_right,bottom_left,bottom_right)

    
    # Calculate the center of the rectangle
    center_x = top_left[0] + top_right[0] // 2
    center_y = top_left[1] + bottom_left[0] // 2
    
    return center_x, center_y

# Open the video file
cap = cv2.VideoCapture('Videos\moving_rectangle.avi')

# Initialize trackImage to store trajectory
trackImage = np.zeros((1200, 1200, 3), np.uint8)


while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Call the detect_rectangle function for each frame
    center_x, center_y = detect_rectangle(gray_frame)
    
    # Draw a circle at the detected center coordinates on trackImage
    trackImage = cv2.circle(trackImage, (center_x, center_y), radius=1, color=(0, 0, 255), thickness=1)

    # Display the center coordinates
    print("Center coordinates:", (center_x, center_y))
    
    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# # Resize the trajectory image to fit the screen
trackImage_resized = cv2.resize(trackImage, (800, 700))

# Display the resized trajectory image
cv2.imshow("Trajectory", trackImage)
cv2.waitKey(0)

# Release everything when done
cap.release()
cv2.destroyAllWindows()