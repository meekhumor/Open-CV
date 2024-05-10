import cv2 as cv
import numpy as np

img = cv.imread('Images/bahubali.jpg')
cv.imshow('real', img)
# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)