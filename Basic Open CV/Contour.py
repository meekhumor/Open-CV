import cv2 as cv
import numpy as np

img = cv.imread('Images/dog_test.png')
cv.imshow('real', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours,heirarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# RETR_LIST for all contours
# RETR_EXTERNAL for all contours
# RETR_TREE for all heirarchical contours
print(f'{len(contours)} is no. of contours we found')

cv.drawContours(blank, contours, -1, (0,0,255), thickness=2) 
# -1 indicates that we want to draw all contours
cv.imshow('Contours drawn', blank)


cv.waitKey(0)