import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper range for a color (e.g., blue)
lower_bound = np.array([100, 150, 50])   # Lower bound for blue in HSV
upper_bound = np.array([140, 255, 255])  # Upper bound for blue in HSV

# Create a mask using inRange
mask = cv2.inRange(hsv, lower_bound, upper_bound)

# Apply the mask to extract the color
result = cv2.bitwise_and(image, image, mask=mask)

# Display the original image, mask, and result
cv2.imshow("Original Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Filtered Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
