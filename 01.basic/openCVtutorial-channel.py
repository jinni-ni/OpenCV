import cv2
import numpy as np

print("OpenCV version:")
print(cv2.__version__)

img = cv2.imread("./image/marathon_01.jpg")

print("width: {} pixcels".format(img.shape[1]))
print("height: {} pixcels".format(img.shape[0]))
print("channels; {}".format(img.shape[2]))

(height, width) = img.shape[:2]
center = (width //2, height // 2)

cv2.imshow("test", img)

## R G B

(Blue, Green, Red) = cv2.split(img)

cv2.imshow("Red channel", Red)
cv2.imshow("Green channel", Green)
cv2.imshow("Blue channel", Blue)
cv2.waitKey(0)

### RGB
zeros = np.zeros(img.shape[:2], dtype="uint8")
cv2.imshow("red", cv2.merge([zeros, zeros, Red]))
cv2.imshow("green", cv2.merge([zeros, Green, zeros]))
cv2.imshow("blue", cv2.merge([Blue, zeros, zeros]))

## filter
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Filter", gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Filter", hsv)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB Filter", lab)

## merge
BGR = cv2.merge([Blue, Green, Red])
cv2.imshow("Blue, Green and Red", BGR)

cv2.waitKey(0)
cv2.destroyAllWindows()

