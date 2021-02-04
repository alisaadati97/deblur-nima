import sys 

import cv2
import numpy as np


def find_blured_object(obj):
    """this function get the object and subtract the frame with object from the one witout object
     then threshold the values so the pixels near black (0,0,0) will get black 
     and with a median filter only the object will remain"""
    
    if obj == "mouse":
        back = cv2.imread("mouse_78.png")
        blur = cv2.imread("mouse_81.png")

    elif obj== "shoe":
        back = cv2.imread("shoe_35.png")
        blur = cv2.imread("shoe_39.png")


    diff = cv2.absdiff(back, blur)

    mask = cv2.inRange(diff, np.array([15,15,15]), np.array([255,255,255]))
    res = cv2.bitwise_and(blur,blur, mask= mask)

    median = cv2.medianBlur(res,5)
    mask = cv2.inRange(median, np.array([1,1,1]), np.array([255,255,255]))

    _ , contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(cnt)
    median = cv2.rectangle(median,(x,y),(x+w,y+h),(0,255,0),2)

    #create a black background with the shape of original frame
    black = np.zeros((res.shape[0],res.shape[1],3), np.uint8)



    for i  in  range(y , y+h):
        for j in range( x , x+w ):
            #black[i][j] = blur[i][j]
            black[i][j] = median[i][j]
            #median[i][j] = blur[i][j]
    
    canny = cv2.Canny(black,100,200)
    mask = cv2.inRange(black, np.array([1,1,1]), np.array([255,255,255]))

    #cv2.imwrite("image.png" , res)

    cv2.imshow('median',median)
    cv2.imshow('res',res)
    cv2.imshow('canny',canny)
    cv2.imshow('black',black)

    cv2.waitKey()
    
    
    


if __name__ == "__main__":
    find_blured_object( sys.argv[1] )