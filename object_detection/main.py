from detector import * 
import cv2 as cv

imageLists = ['cat-dog','fruits',"street","pizza","room"]

detctor = Detector()
for imgName in imageLists :
    img = cv.imread("images/{}.jpg".format(imgName))
    img = detctor.detect(img)
    cv.imshow(imgName , img)
cv.waitKey()







