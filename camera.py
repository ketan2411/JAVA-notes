import cv2
import time
cap=cv2.VideoCapture(0)
status,frame=cap.read()
print(frame.shape)
cv2.imshow('windowname',frame)
cv2.waitKey(0)
