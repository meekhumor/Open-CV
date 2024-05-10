import cv2 as cv
import numpy as np

img = cv.imread('Images/bahubali.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('real', img)

b,g,r = cv.split(img)


cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

# region where it is lighter shows that there is more contribution of that channels and vice versa

merge = cv.merge([b,g,r])
cv.imshow('merged', merge)

blue = cv.merge([b,blank,blank])
cv.imshow('blue', blue)
green = cv.merge([blank,g,blank])
cv.imshow('green', green)
red = cv.merge([blank,blank,r])
cv.imshow('red', red)


cv.waitKey(0)

