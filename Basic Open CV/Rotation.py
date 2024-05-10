import cv2 as cv
import numpy as np

img = cv.imread('Images/dog_test.png')
cv.imshow('real', img)

def rotate(img, angle, rotationPoint = None):
    (height,width) = img.shape[:2] # :2 refers to first two values
    
    if rotationPoint is None:
        rotationPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotationPoint, angle, scale=1.0)
    dim = (width,height)

    return cv.warpAffine(img, rotMat, dim)
    
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

cv.waitKey(0)