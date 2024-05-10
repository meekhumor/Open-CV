import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture('Videos\m_face1.mp4')
pTime = 0
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

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

    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img_resized, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec,drawSpec)
        for id,lm in enumerate(faceLms.landmark):
            #print(lm)
            ih, iw, ic = img.shape
            x,y = int(lm.x*iw), int(lm.y*ih)
            print(id,x,y)


    # to check FPS and display it on screen
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img_resized, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN,3, (0, 255, 0), 2) # f'{}' is template literals

    cv.imshow("Image", img_resized)
    cv.waitKey(1)
