import cv2 as cv
import numpy as np

img = cv.imread('Images/kohli-cover-drive-kolkta1.jpg')
cv.imshow('real', img)

def rescaleFrame(frame, scale = 0.75):
    # works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized = rescaleFrame(img)

# Averaging
average = cv.blur(resized, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(resized, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(resized, 3)
cv.imshow('Median Blur', median)

# Bilateral 
# Best method, you can retain edges as well
bilateral = cv.bilateralFilter(resized, 10, 35, 25) # (img, diameter, sigmaColor, sigmaSpace)

# sigmaColor: larger values for this means that there are more colors in neighbourhood that will be considered when blur is computed
# sigmaSpace: larger values of this means that pixels further out from central pixel will influence blurring calculation

cv.imshow('Bilateral', bilateral)

cv.waitKey(0)