import cv2 as cv
import numpy as np

img = cv.imread('Images/dog_test.png')
cv.imshow('real', img)

def translate(img,x,y): # x refers to number of pixel to be shifted in x axis same with y
    transMat = np.float32([[1,0,x],[0,1,y]])
    dim =  (img.shape[1],img.shape[0])

    return cv.warpAffine(img, transMat, dim)

# -x -> left
#  x -> right
# -y -> down
#  y -> up

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

cv.waitKey(0)