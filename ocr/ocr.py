import pytesseract
import cv2 as cv 
from pytesseract import Output

TRESHOLD = 10 
pytesseract.pytesseract.tesseract_cmd = 'E:/ocr/tesseract.exe'  

def drowBoxs(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        # print(results["text"][i])
        # print(int(float(d['conf'][i])))
        if int(float(d['conf'][i])) > TRESHOLD:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img 

def getText(img):
    return pytesseract.image_to_string(img)  

def showImage(img,waitValue=0):
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    cv.imshow("img" , img)
    cv.waitKey(waitValue)



