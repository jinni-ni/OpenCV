import cv2

print("OpenCV version:")
print(cv2.__version__)

img = cv2.imread("./image/marathon_01.jpg")

print("width: {} pixcels".format(img.shape[1]))
print("height: {} pixcels".format(img.shape[0]))
print("channels; {}".format(img.shape[2]))
      
cv2.imshow("test",img)

cv2.waitKey(0)
cv2.imwrtie("test.jpg",img)
cv2.destroyAllWindows()
