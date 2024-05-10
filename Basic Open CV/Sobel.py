import cv2
import numpy as np
image = cv2.imread('Images/contour1.jpg')

# Sobel X filter
# [1  0 -1]
# [2  0 -2]
# [1  0 -1]

#--------------------------------------------
# sobel_x = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
# horizontal_edge_image = cv2.filter2D(image,-1,sobel_x)
# cv2.imshow('Horizontal',horizontal_edge_image)
# cv2.imshow('Sudoku',image)
#--------------------------------------------

# Sobel Y filter
# [ 1   2   1]
# [ 0   0   0]
# [-1  -2  -1]

#--------------------------------------------
sobel_y = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
vertical_edge_image = cv2.filter2D(image,-1,sobel_y)
cv2.imshow('Vertical',vertical_edge_image)
cv2.imshow('Sudoku',image)
#---------------------------------------------

# HighPass Filter
# [0  1  0]
# [1 -4  1]
# [0  1  0]

#--------------------------------------------
# highpass = np.array([[0,1,0],[1,-4,1],[0,1,0]])
# highpass_edge = cv2.filter2D(image,-1,highpass)
# cv2.imshow('HighPass',highpass_edge)
# cv2.imshow('Sudoku',image)
# --------------------------------------------

# Thresholding
#--------------------------------------------
# eye = cv2.imread('Images/contour2.jpg')
# greyscale = cv2.imread('Images/contour2.jpg',0)
# avg = np.average(greyscale) # we get average of whole array this will be our threshold value
# ret, thresh = cv2.threshold(greyscale,avg,255,cv2.THRESH_BINARY) #(greyscale, threshold, maximum, binarize)
# cv2.imshow('Eye Image',eye)
# cv2.imshow('Greyscale',greyscale)
# cv2.imshow('Threshold',thresh)
#--------------------------------------------

# Contours 
#--------------------------------------------
# greyscale_sudoku = cv2.imread('Images/contour1.jpg',0)
# avg = np.average(greyscale_sudoku)
# ret, thresh_sudoku = cv2.threshold(greyscale_sudoku,avg,255,cv2.THRESH_BINARY)
# contours,hierarchy = cv2.findContours(greyscale_sudoku,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# final = cv2.drawContours(image,contours,-1,(0,255,0),3)
# cv2.imshow('Contour',final)
# cv2.imshow('Sudoku',image)
#----------------------------------------------
cv2.waitKey(0)