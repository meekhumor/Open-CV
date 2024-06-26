import cv2 as cv

# img = cv.imread('Images/bahubali.jpg')
img = cv.imread('task3_pics\\tc2-3.png')
cv.imshow('real', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# compare each pixels of image with a thresholding value and if it has less than threshold value, we set that pixel intensity to zero which is black 

# Simple Thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV ) # threshold will have same value which we are passing
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Since we are giving threshold value by ourselves it will not be effective so let computer decide it

# Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9) 
# (img, max, adaptive method, threshold type, kernel size, integer to substracted from mean)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)