import cv2 as cv
import numpy as np

img = cv.imread('Images/dog_test.png')
cv.imshow('real', img)

cropped = img[200:400, 300:400] 
cv.imshow('crop', cropped)

cv.waitKey(0)