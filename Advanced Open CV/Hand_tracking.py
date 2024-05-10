import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands( max_num_hands=5)
mpDraw = mp.solutions.drawing_utils # for drawing the points on the landmarks

cTime = 0
pTime = 0

while True: 
    success, img = cap.read()

    # flipping the image
    flipimg = cv.flip(img,1)

    # converting the flipped image to rgb
    imgRGB = cv.cvtColor(flipimg,cv.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    # this will process the frame for us and store it in results

    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark): 
                # id is a specific point such as tip of index finger will have a id
                # Lm contains the x, y coordinates of specific id
                # print(id, lm)
                h, w, c = flipimg.shape # extracting the height and width of flipped image
                cx, cy = int(lm.x * w), int(lm.y * h) # since lm gives value in ratio basis so we need to multiply it with width and height respectively
                print(id, cx, cy)

                if id == 8:
                    cv.circle(flipimg, (cx, cy), 15, (255, 0, 255), cv.FILLED) # it will make circle around id 4

            mpDraw.draw_landmarks(flipimg,handLms,mphands.HAND_CONNECTIONS) 
            # there could be more than one hand so we draw landmarks in each hand using for loop
            # mphands.HAND_CONNECTIONS for drawing the lines between the landmarks


    cTime = time.time()
    fps = 1 / (cTime - pTime) # Calculating the FPS
    pTime = cTime

    cv.putText(flipimg, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)    # Displaying the FPS


    cv.imshow('Image', flipimg)
    cv.waitKey(1)

