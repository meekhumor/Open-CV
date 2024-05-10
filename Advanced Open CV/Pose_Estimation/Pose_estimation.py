import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
cap = cv.VideoCapture('Videos\pose2.mp4')
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB) # convert the image to RGB
    results = pose.process(imgRGB)

    print(results.pose_landmarks) # it has x,y and visibility details in it

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # this will draw points and POSE_CONNECTIONS will connect these
        for id, lm in enumerate(results.pose_landmarks.landmark): # it consist of all points
            h, w, c = img.shape
            print(id,lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)

    # to check FPS and display it on screen
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3)

    cv.imshow("Image", img)
    cv.waitKey(1)

    