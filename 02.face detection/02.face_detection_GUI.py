import cv2
import numpy as np

from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog


face_cascade_name = '../cv2/data/haarcascade_frontalface_alt.xml'
eyes_cascade_name = '../cv2/data/haarcascade_eye_tree_eyeglasses.xml'
file_name = 'image/marathon_01.jpg'
title_name='Hear cascade object detection'
frame_width = 500



def selectFile():
    file_name = filedialog.askopenfilename(initialdir = "./image", title="select file", filetypes = (("jpeg files", "*.jpg"), ("all files","*.*")))
    print('file name: ', file_name)
    read_image = cv2.imread(file_name)
    (height, width) = read_image.shape[:2]
    frameSize = int(sizeSpin.get())
    ratio = frameSize / width
    dimension = (frameSize, int(height * ratio))
    read_image = cv2.resize(read_image, dimension, interpolation =  cv2.INTER_AREA)
    
    image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)

    detectAndDisplay(read_image)

def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
            
    #cv2.imshow('Capture - Face detection', frame)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)
    detection.config(image=imgtk)
    detection.image = imgtk
    



## main
main = Tk()
main.title(title_name)
main.geometry()

#print("version:")
#print(cv2.__version__)

read_image = cv2.imread("../image/marathon_01.jpg")

#print("width: {} pixcels".format(img.shape[1]))
#print("height: {} pixcels".format(img.shape[0]))
#print("channels; {}".format(img.shape[2]))

(height, width) = read_image.shape[:2]

## resize
ratio = frame_width / width
dimension = ( frame_width, int(height * ratio))
read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)

image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
imgtk = ImageTk.PhotoImage(image=image)


face_cascade_name = '../cv2/data/haarcascade_frontalface_alt.xml'
eyes_cascade_name = '../cv2/data/haarcascade_eye_tree_eyeglasses.xml'

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)


label = Label(main, text=title_name)
label.config(font=("Courier", 18))
label.grid(row=0, column=0, columnspan=4)
sizeLabel=Label(main, text='Frame width: ')
sizeLabel.grid(row=1,column=0)
sizeVal = IntVar(value=frame_width)
sizeSpin = Spinbox(main, textvariable=sizeVal, from_=0, to=2000, increment=100, justify=RIGHT)
sizeSpin.grid(row=1, column=1)
Button(main, text="file seelct", height=2, command=lambda:selectFile()).grid(row=1, column=2, columnspan=2)
detection=Label(main, image=imgtk)
detection.grid(row=2,column=0, columnspan=4)
detectAndDisplay(read_image)

