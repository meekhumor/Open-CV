import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8') # makes a blank image 
# 3 is basically channels we are providing which is R G B
cv.imshow('Blank', blank)

# Paint the image with a certain colors
# blank[:] = 0,255,0 
# cv.imshow('Green', blank)

# blank[100:200, 200:300] = 0,0,255 # 200 to 300 in y axis and 300 to 400 in x axis
# cv.imshow('Red', blank)

# Draw a rectangle
cv.rectangle(blank,(0,0), (250,250), (0,0,255), thickness = cv.FILLED)
cv.imshow('Blue Rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,(255,0,0), thickness = -1) #(img, location, size,color,thickness)
cv.imshow('Circle', blank)

#Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness = 3)
cv.imshow('Line', blank)

cv.putText(blank, 'Hello', (225,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,0), 2) #(img, text,font-family, scale, color, thickness)
cv.imshow('Text', blank)          

cv.waitKey(0)
