import cv2
import numpy as np

img= cv2.imread("bookpage.jpg")

returnval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

greyscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
returnval2,threshold2=cv2.threshold(greyscaled,12,255,cv2.THRESH_BINARY)
gaus =cv2.adaptiveThreshold(greyscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) #THRESHOLD 3 (ADAPTIVE THRESHOLD)
cv2.imshow("original",img)
cv2.imshow("threshold",threshold)
cv2.imshow("threshold2",threshold2)
cv2.imshow("gauss",gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
