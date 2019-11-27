from PIL import Image
import pytesseract
import argparse
import cv2
import os


def ocr(x1, x2, y1, y2):
    """!
    @detailed extracting content out of the bill receipt
    @return String text-from-image
    """
    x1 = int(float(str(x1)))  
    y1 = int(float(str(y1))) 
    x2 = int(float(str(x2))) 
    y2 = int(float(str(y2)))   
    image = cv2.imread('abcd.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = Image.open("abcd.jpg")
    gray = gray.crop((x1, y1, x2, y2))
    gray.save("temp.jpeg")
    text = pytesseract.image_to_string(Image.open("temp.jpeg"))
    return text




