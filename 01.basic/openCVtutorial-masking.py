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

# img size 0 array
mask = np.zeros(img.shape[:2], dtype='uint8')

# img circle white 
cv2.circle(mask, center, 300, (255, 255, 255), -1)
cv2.imshow("mask",mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("nomad with mask", masked)


cv2.waitKey(0)
cv2.destroyAllWindows()

