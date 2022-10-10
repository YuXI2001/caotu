import cv2  
img = cv2.imread("photo.png")  #图片路径
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
inverted_gray_image = 255-gray_image  
blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19,19),0)  
inverted_blurred_image = 255-blurred_inverted_gray_image  
sketck = cv2.divide(gray_image, inverted_blurred_image,scale= 256.0)  
cv2.imshow("Original Image",img)  
cv2.imshow("Pencil Sketch", sketck)  
cv2.waitKey(0)
