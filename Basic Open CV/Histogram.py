import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Histogram allows you to visualize the pixel intensity in an image
# Pixel intensity refers to the brightness or darkness of a pixel in a digital image. 
# Each pixel corresponds to an intensity value, which is a numerical representation of its brightness.
# In most digital images, intensity values range from 0 to 255.

img = cv.imread('Images/bahubali.jpg')
cv.imshow('real', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)

# Grayscale histogram
# konse no. k pixel jyada hai woh batata hai jaise 255(white) kitna hai

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] ) # (img, channels{0, since this is grayscale}, mask, histSize, range{0 to 256})

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour Histogram

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)