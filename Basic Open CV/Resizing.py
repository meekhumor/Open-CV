import cv2 as cv

# Resizing function
def rescaleFrame(frame, scale = 0.75):
    # works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Reading images
img = cv.imread('Images/bahubali.jpg')
cv.imshow('Cat', img)

# Changing resolution
def changeRes(width,height):
    # Only works for live video
    capture.set(3,width) # 3 references the width
    capture.set(4,height) # 4 references the height


# Reading videos
capture = cv.VideoCapture('Videos/moving_rectangle.avi') # In argument 0 is to access first camera, while 1 is for additional and so on 

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame) # frame gets resized you can also provide scale to it

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)