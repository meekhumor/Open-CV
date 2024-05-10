# import cv2 as cv
# import mediapipe as mp
# import time

# class handDetector():
#     def __init__(self, mode=False, maxHands=2, detectionCon=1, trackCon=1): # these are default parameter for class hanDetector
#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.detectionCon, self.trackCon)
#         self.mpDraw = mp.solutions.drawing_utils

#     def findHands(self, img, draw=True):
#         imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)
#         # print(results.multi_hand_landmarks)
#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
#         return img
    
#     # def findPosition(self, img, handNo=0, draw=True):
#     #     lmList = []
#     #     if self.results.multi_hand_landmarks:
#     #         myHand = self.results.multi_hand_landmarks[handNo]
#     #         for id, lm in enumerate(myHand.landmark):
#     #             # print(id, lm)
#     #             h, w, c = img.shape
#     #             cx, cy = int(lm.x * w), int(lm.y * h)
#     #             # print(id, cx, cy)
#     #             lmList.append([id, cx, cy])
#     #             if draw:
#     #                 cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
#     #     return lmList

# # dummy code just to check how this module works
# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv.VideoCapture(0)
#     detector = handDetector()
    
#     while True:
#         success, img = cap.read()
#         flipimg = cv.flip(img,1)

#         mimg = detector.findHands(flipimg)
#         # lmList = detector.findPosition(flipimg)
#         # if len(lmList) != 0:
#         #     print(lmList[4])


#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#         cv.putText(mimg, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
#         cv.imshow("Image", mimg)
#         cv.waitKey(1)

# if __name__ == "__main__":
#     main()

import cv2
import mediapipe as mp
import time
class handDetector():
    def __init__(self, maxHands=6):
        self.maxHands = maxHands
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.maxHands)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
    