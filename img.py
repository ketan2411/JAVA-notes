import cv2
img=cv2.imread('car.jpg')
imgnew=img[0:100,0:300]
print(imgnew)
print(img.shape)
cv2.line(imgnew,(0,0),(300,400),(0,0,255))
cv2.imshow('windowname',imgnew)
cv2.waitKey(0)
