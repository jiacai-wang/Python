import cv2
rgb = cv2.imread("./rgb.png",)
yuv = cv2.cvtColor(rgb,cv2.COLOR_BGR2YUV)
cv2.imshow("yuv",yuv)
cv2.imshow("rgb",rgb)
cv2.waitKey()
cv2.imwrite("./yuv.bmp",yuv)
cv2.imwrite("./rgb.bmp",rgb)