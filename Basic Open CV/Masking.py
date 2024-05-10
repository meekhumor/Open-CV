import cv2 as cv
import numpy as np

img = cv.imread('Images/bahubali.jpg')
cv.imshow('real', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape) 
# above line says mask the img with weird_shape and save it in img 
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)