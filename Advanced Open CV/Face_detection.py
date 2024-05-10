import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture('Videos/multiple_faces.mp4')
pTime = 0
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

def rescaleFrame(frame, scale = 0.2):
    # works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


while True:
    success, img = cap.read()

    img_resized = rescaleFrame(img) # frame gets resized you can also provide scale to it
    imgRGB = cv.cvtColor(img_resized, cv.COLOR_BGR2RGB)

    results = faceDetection.process(imgRGB)
    # print(results)

    if results.detections:
        for id, detection in enumerate(results.detections): # can detect multiple face 
            # mpDraw.draw_detection(img, detection)
            # print(id, detection) # detection is object which contains score, relative_bounding_box, relative keypoints
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box) # this contains the location of xmin, ymin, width and height

            bboxC = detection.location_data.relative_bounding_box # we stored it in bboxC now it contains xmin, ymin, width and height
            ih, iw, ic = img_resized.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih) # converted the values in pixels and stored it in bbox

            cv.rectangle(img_resized, bbox, (255, 0, 255), 2) # made a rectangle using this value
            cv.putText(img_resized, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2) # printed % match

    # to check FPS and display it on screen
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img_resized, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN,3, (0, 255, 0), 2) # f'{}' is template literals

    cv.imshow("Image", img_resized)
    cv.waitKey(1)
