from asyncio.windows_events import NULL
import cv2 as cv 
import ocr as Ocr



def saveToFile(pageNum,text):
    with open("text.txt", "a") as file:
        file.write("="*20 + str(pageNum) + "="*20 + "\n" + text)


vid = cv.VideoCapture("images/video.mp4")
prevText = NULL 
pageNum = 0 
print("start detection")
while True :
    state,frame = vid.read()
    print(state)
    if state== False : break 
    text = Ocr.getText(frame)
    if(text != prevText):
        pageNum += 1
        print("new page detect : " + str(pageNum))
        saveToFile(pageNum,text)
        prevText = text
    
    img = Ocr.drowBoxs(frame)
    Ocr.showImage(img,waitValue=1)
  

vid.release()
cv.destroyAllWindows()
# image = cv.imread('images/test2.png')
# text = Ocr.getText(image)
# print("Detected text is : "+text)
# image = Ocr.drowBoxs(image)
# Ocr.showImage(image)


