from asyncio.windows_events import NULL
import cv2 as cv 
import ocr as Ocr


vid = cv.VideoCapture(0)
prevText = NULL 

while True :
    state,frame = vid.read()
    text = Ocr.getText(frame)
    if(text != prevText):
        print("Detected text is : "+text)
        prevText = text
    
    frame = Ocr.drowBoxs(frame)
    Ocr.showImage(frame,waitValue=1)


# image = cv.imread('test.png')
# text = Ocr.getText(image)
# print("Detected text is : "+text)
# image = Ocr.drowBoxs(image)
# Ocr.showImage(image)


