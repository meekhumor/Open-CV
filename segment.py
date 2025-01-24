import cv2

# Function to get the pixel value (0 or 1) at a specific position with boundary checks
def get_pixel_value(x, y, img):
    height, width = img.shape[:2]  # Use only the first two dimensions (height, width)
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0  # Out of bounds, return 0
    return 1 if img[y, x] > 0 else 0  # Assuming non-zero is 1 and zero is 0

# Function to generate the string of pixel values
def generate_pixel_string(img, start_x=12, start_y=12, steps=4, move_x=25, move_y=25):
    # Convert the image to grayscale if it is not already
    if len(img.shape) == 3:  # Check if it's a color image (3 channels)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x, y = start_x, start_y  # Starting coordinates
    pixel_values = ""
    pixel_values += str(get_pixel_value(x, y, img))  # Collect initial pixel value

    # Draw a circle at the starting point (12, 12)
    cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Green circle with radius 5

    # Loop for 4 steps of the pattern
    for _ in range(steps):
        x += move_x  # Move right by 'move_x' pixels

        # Collect color at the new position
        pixel_values += str(get_pixel_value(x, y, img))

        # Draw a circle at the new position
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Green circle with radius 5

        y += move_y
        x -= move_x

        pixel_values += str(get_pixel_value(x, y, img))

        # Draw a circle at the new position
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Green circle with radius 5

    # Remove the last element from the string
    pixel_values = pixel_values[:-1]
    
    return pixel_values

# Load the image in grayscale (0)
img = cv2.imread('seg.png', 0)

# Convert to color to draw colored lines
colored_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Generate pixel string
pixel_string = generate_pixel_string(colored_img)

# Print the collected pixel values
print("Collected pixel values:", pixel_string)

# Display the image with circles
cv2.imshow('Image with Circles', colored_img)

# Wait for any key press
cv2.waitKey(0)

