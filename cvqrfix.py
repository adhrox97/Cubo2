import cv2
import numpy as np
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimgu

#Inicializar la camara
capture = cv2.VideoCapture(0)

 
#Cargar la fuente
font = cv2.FONT_HERSHEY_SIMPLEX

while 1:

    val, frame  = capture.read()

    def display(im, bbox):
        n = len(bbox)
        for j in range(n):
            cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (0,0,255), 3)
        
        # Display results
        cv2.imshow("Results", im)

    qrDecoder = cv2.QRCodeDetector()
        
    # Detect and decode the qrcode
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)

    if len(data)>0:
        dato=data
        print("Decoded Data : {}".format(data))
        display(frame, bbox)
        
        if dato == "hola":
            
            cv2.destroyAllWindows()
            img = cv2.imread('colombia.jpg', cv2.IMREAD_COLOR)
            imS = cv2.resize(img, (640, 480))
            cv2.imshow('colombia', imS)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            continue
        
        elif dato == "adios":
            
            cv2.destroyAllWindows()
            img = cv2.imread('espana.jpg', cv2.IMREAD_COLOR)
            imS = cv2.resize(img, (640, 480))
            cv2.imshow('espana', imS)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            continue
    else:
        print("QR Code not detected")
        cv2.imshow("Results", frame)
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


#if dato == "hola":
#    
#    img = cv2.imread('colombia.jpg', cv2.IMREAD_COLOR)
#    imS = cv2.resize(img, (640, 480))
#    cv2.imshow('titulo', imS)
#    cv2.waitKey(0)