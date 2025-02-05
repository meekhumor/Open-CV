import cv2
import numpy as np

img = cv2.imread('Projects/QR_Extractor/QR2.png', 0)
resized_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  
rotated_img = cv2.rotate(resized_img, cv2.ROTATE_180) 

height, width = rotated_img.shape
colored_img = cv2.cvtColor(rotated_img, cv2.COLOR_GRAY2BGR)


for x in range(0, width, 50):
    cv2.line(colored_img, (x, 0), (x, height), (0, 255, 0), 1)  

for y in range(0, height, 100):
    cv2.line(colored_img, (0, y), (width, y), (255, 0, 0), 1)  

def get_pixel_value(x, y, img):
    height, width = img.shape[:2]  
    if x < 0 or x >= width or y < 0 or y >= height:
        return 0  
    return 1 if img[y, x] > 0 else 0  


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

def binary_to_text_with_steps(binary_input):
     # Ensure the input is exactly 8 bits
    if len(binary_input) != 8:
        raise ValueError("Input binary must be 8 bits long")
    
    # Convert the binary string to a decimal value
    decimal_value = int(binary_input, 2)
    
    # Convert the decimal value to its ASCII character equivalent
    ascii_char = chr(decimal_value)
    
    return ascii_char





# Function to extract segments with zigzag movement
def extract_segments(image, segment_width, segment_height, stride_width, stride_height):
    segments = []
    h, w = image.shape
    ans = ""
    binary_string = ""
    flip_required = False 

    for x in range(0, w - segment_width + 1, stride_width):  # Move right (stride of 50)
        # Move down for even columns, up for odd columns
        if (x // stride_width) % 2 == 0:  # Move down for even columns
            y_range = range(0, h - segment_height + 1, stride_height)  # Downward movement
        else:  # Move up for odd columns
            y_range = range(h - segment_height, -1, -stride_height)  # Upward movement

        for y in y_range:
            segment = image[y:y + segment_height, x:x + segment_width]

            if flip_required:
                segment = cv2.flip(segment, 0) 

            binary_code = generate_pixel_string(segment)
            text = binary_to_text_with_steps(binary_code)
            binary_string += binary_code
            ans += text
            segments.append(segment)
        flip_required = not flip_required
        
    return ans

cv2.imshow("rotate", rotated_img)

# Extract segments of 50x100 with strides of 50 for width and 100 for height
answer = extract_segments(rotated_img, 50, 100, 50, 100)

# # Display the first segment for verification
# if segments:
#     cv2.imshow("First Segment", segments[15])  # Display the first segment


print(answer)
# print(f"Extracted {len(segments)} segments of size 50x100.")

# Display the segmented image with lines
cv2.imshow("Segmented Image", colored_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
