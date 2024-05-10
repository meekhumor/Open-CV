import cv2 as cv 
import mediapipe as mp
import time

def rescaleFrame(frame, scale = 0.2):
    # works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

class FaceMeshDetector():

    def __init__(self, maxFaces=2):
        self.maxFaces = maxFaces

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh()

        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self, img, draw=True):
        self.imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)

        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                face = []
                for id,lm in enumerate(faceLms.landmark):

                    ih, iw, ic = img.shape
                    x,y = int(lm.x*iw), int(lm.y*ih)
                    #cv.putText(img, str(id), (x, y), cv.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 1)

                    #print(id,x,y)
                    face.append([x,y])
                    faces.append(face)
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)
        

        return img, faces

def main():
    cap = cv.VideoCapture("Videos\multiple_faces.mp4")
    pTime = 0
    detector =  FaceMeshDetector(maxFaces=2)

    while True:
        success, img = cap.read()
        img_resized = rescaleFrame(img) # frame gets resized you can also provide scale to it

        img, faces = detector.findFaceMesh(img_resized)
        if len(faces)!= 0:
            print(faces[0])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
        cv.imshow("Image", img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()

