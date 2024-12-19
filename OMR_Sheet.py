import cv2 as cv 
import numpy as np 

img = cv.imread('OMR.png',0)

kernel = np.ones((11, 11), np.uint8)
dilate = cv.dilate(img, kernel, iterations=1)
erode = cv.erode(dilate, kernel, iterations=1)
list1=[]

height = 0
while (height < erode.shape[0] - 1):
    width = 0
    while (width < erode.shape[1] - 1):
        if (erode[height,width] == 0):
            if width>0 and width<erode.shape[1] // 4:
                list1.append("A")
            elif width>erode.shape[1] // 4 and width<2*erode.shape[1] // 4:
                list1.append("B")
            elif width>erode.shape[1]*2 // 4 and width<erode.shape[1]*3 // 4:
                list1.append("C")
            elif width>erode.shape[1]*3 // 4 and width<erode.shape[1]*4 // 4:
                list1.append("D")
            
            height = height + erode.shape[0] // 4
            break
        width = width + 1
    height = height + 1

print(list1)

# vertical lines
cv.line(erode,(erode.shape[1] // 4,0),(erode.shape[1] // 4 ,erode.shape[0]),(0,255,0),2)
cv.line(erode,(2* erode.shape[1] // 4,0),(2 * erode.shape[1] // 4 ,erode.shape[0]),(0,255,0),2)
cv.line(erode,(3* erode.shape[1] // 4,0),(3 * erode.shape[1] // 4 ,erode.shape[0]),(0,255,0),2)
cv.line(erode,(4* erode.shape[1] // 4,0),(4 * erode.shape[1] // 4 ,erode.shape[0]),(0,255,0),2)

# horizontal lines
cv.line(erode,(0, erode.shape[0] // 4),(erode.shape[1], erode.shape[0] // 4),(0,255,0),2)
cv.line(erode,(0, 2 * erode.shape[0] // 4),(erode.shape[1], 2 * erode.shape[0] // 4),(0,255,0),2)
cv.line(erode,(0, 3 * erode.shape[0] // 4),(erode.shape[1], 3 * erode.shape[0] // 4),(0,255,0),2)
cv.line(erode,(0, 4 * erode.shape[0] // 4),(erode.shape[1], 4 * erode.shape[0] // 4),(0,255,0),2)

cv.circle(erode,(5* erode.shape[1] // 8,erode.shape[0] // 8),20,0.5,2)

mask = np.zeros((erode.shape[0], erode.shape[1]), dtype=np.uint8)
center = (5* erode.shape[1] // 8,erode.shape[0] // 8)
radius = 20

mask_inv = cv.bitwise_not(mask)

# Create a white background image
white_background = np.ones_like(erode) * 255

# Combine the white background with the original erode using the inverted mask
white_background = cv.bitwise_and(white_background, white_background, mask=mask_inv)
circular_cropped_image = cv.bitwise_and(erode, erode, mask=mask)
final_image = cv.add(white_background, circular_cropped_image)


# Count the number of black pixels (pixel value 0) inside the circle
black_pixel_count = np.sum(final_image == 0)

print(f'The number of black pixels inside the circle is: {black_pixel_count}')
print(f'Percentage: {black_pixel_count // (np.pi * (radius**2))}')


cv.imshow('masked',final_image)

cv.imshow('erode',img)
cv.imshow('dilation',erode)


cv.waitKey(0)