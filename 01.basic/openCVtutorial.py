import cv2

print("OpenCV version:")
print(cv2.__version__)

img = cv2.imread("./image/marathon_01.jpg")

print("width: {} pixcels".format(img.shape[1]))
print("height: {} pixcels".format(img.shape[0]))
print("channels; {}".format(img.shape[2]))
      
cv2.imshow("test",img)

(b, g, r) = img[0, 0]

print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

dot = img[50:100, 50:100]
#cv2.imshow("Dot", dot)

img[50:100, 50:100] = (0, 0, 255)
#cv2.imshow("nomade -dotted",img)


cv2.rectangle(img, (150,50), (200,100), (0, 255, 0), 5)
#cv2.imshow("nomade -rectangle",img)

cv2.circle(img, (275, 75), 25, (0, 255, 255), -1)
#cv2.imshow("nomade -circle",img)

cv2.line(img, (350, 100), (400, 100), (255, 0, 0), 5)
#cv2.imshow("nomade -line",img)

cv2.putText(img, 'developer.jin', (450, 100,), cv2.FONT_HERSHEY_COMPLEX, 1,(255, 255,  255), 4)
cv2.imshow("nomade -font",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

