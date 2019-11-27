from PIL import Image
import pytesseract
import argparse
import cv2
import os


def ocr(x1, x2, y1, y2):

    x1 = int(float(str(x1)))  
    y1 = int(float(str(y1))) 
    x2 = int(float(str(x2))) 
    y2 = int(float(str(y2)))   
    image = cv2.imread('abcd.jpg')






    print(x1, x2, y1, y2)
    
    #image.save('test.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    gray = Image.open("abcd.jpg")
    gray = gray.crop((x1, y1, x2, y2))
    # img2.save("img2.jpg")

    gray.save("temp.jpeg")

    # gray = gray[y1:y2, x1:x2]
    #filename = ("img.jpg").format(os.getpid())
    #cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open("temp.jpeg"))
    return text




