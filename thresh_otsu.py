#1.图a,b,在b上加a
#2.读取，求mask,mask_inv,a and inv,b and mask,b+a
#3.threshold不用otus滤波
import cv2

picA=cv2.imread("D:\\a.png")
picB=cv2.imread("D:\\b.png")

imgA_gray=cv2.cvtColor(picA,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(imgA_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
mask_inv=cv2.bitwise_not(mask)

forePic=cv2.bitwise_and(picA,picA,mask=mask_inv)
bgPic=cv2.bitwise_and(picB,picB,mask=mask)
dst=cv2.add(bgPic,forePic)

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()