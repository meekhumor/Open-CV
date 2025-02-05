import cv2 as cv
import numpy as np

# img = cv.imread('Images/bahubali.jpg')
img = cv.imread('1.jpg')
img = cv.resize(img, (1000,1000))
# cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F) # (image, data depth)
lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)//////////////////

# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # (image, data depth, x-direction, y-direction) since y-direction is 0 therefore it's sobel x filter
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)
# cv.imshow('Combined Sobel', combined_sobel)

threshold, thresh_inv = cv.threshold(sobelx, 60, 255, cv.THRESH_BINARY_INV ) # threshold will have same value which we are passing
cv.imshow('Simple Thresholded Inverse', thresh_inv)

kernel = np.ones((3, 3), np.uint8)

# Apply erosion
eroded_image = cv.erode(thresh_inv, kernel, iterations=2)
eroded_image = cv.dilate(thresh_inv, kernel, iterations=1)
eroded_image = cv.erode(thresh_inv, kernel, iterations=1)



cv.imshow("dilate",eroded_image)

canny = cv.Canny(gray, 150, 175)
# cv.imshow('Canny', canny)
cv.waitKey(0)