import cv2

# Callback function to draw red circles
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEWHEEL :  # Right mouse button click
        # Draw an empty red circle
        cv2.circle(image, (x, y), 20, (0, 255, 255), 2)
        cv2.imshow("Image", image)

# Load the image
image_path = "Images/bahubali.jpg"  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load the image. Please check the file path.")
    exit()

# Display the image in a window
cv2.imshow("Image", image)

# Set mouse callback
cv2.setMouseCallback("Image", draw_circle)

# # Wait for a key press
while True:
    if cv2.waitKey(1) & 0xFF == 113:  # Press 'ESC' to exit
        break

# Close all OpenCV windows
cv2.destroyAllWindows()