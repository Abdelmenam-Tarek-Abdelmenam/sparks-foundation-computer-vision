from detector import * 
import cv2 as cv

detctor = Detector()
vid = cv.VideoCapture(0)


while True :
    state,frame = vid.read()
    detctor.detect(frame)

# cv.destroyAllWindows()







