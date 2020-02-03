import cv2
#motion detect function
def mdetect(x,y,z):
    #DIFF OF FIRST TWO TAKE
    fir_diff=cv2.absdiff(x,y) #using absdiff
    sec_diff=cv2.absdiff(y,z) #using absdiff
    #bitwise diff of relative image
    final=cv2.bitwise_and(f_diff,sec_diff)
    return final
