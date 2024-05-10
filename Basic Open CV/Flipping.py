import cv2 as cv
import numpy as np

img = cv.imread('Images/dog_test.png')
cv.imshow('real', img)

flip = cv.flip(img, 0) 
# 0 to flip it verticallys
# 1 to flip it horizontally
# -1 to fip it vertically as well as horizontally

cv.imshow('flip', flip)

cv.waitKey(0)