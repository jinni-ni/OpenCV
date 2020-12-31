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

## moved
#move = np.float32([[1, 0, 100], [0, 1, 100]])
#moved = cv2.warpAffine(img, move, (width, height))
#cv2.imshow("Moved down: +, up: - and right: +, left - ", moved)

## rotate
#move = cv2.getRotationMatrix2D(center, -90, 1.0)
#rotated = cv2.warpAffine(img, move, (width, height))
#cv2.imshow("rotated degress", rotated)

## resize
#ratio = 200.0 / width
#dimension = (200, int(height * ratio))

#resized = cv2.resize(img,dimension, interpolation = cv2.INTER_AREA)
#cv2.imshow("Resized", resized)

## flip
#flipped = cv2.flip(img, -1)
flipped = cv2.flip(img, 1)
#flipped = cv2.flip(img, 0)
cv2.imshow("Fipped", flipped)


cv2.waitKey(0)
cv2.destroyAllWindows()

