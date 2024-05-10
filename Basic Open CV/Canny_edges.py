import cv2 as cv

img = cv.imread('Images/Convolution0.png')
cv.imshow('Tree', img)

# Edge Cascade
canny = cv.Canny(img, 125,175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1) # (img, kernel, iterations)
cv.imshow('Canny Dilation', dilated)

cv.waitKey(0)