# first to import opencv-python
import cv2 as opencv  # opencv-python
import sys

# second thing to define our classifier
defineClassifier = opencv.CascadeClassifier("haarcascade_frontalface_default.xml")

# third thing we need use our image
img = opencv.VideoCapture("img/download1.jpg")

# print(img)
# sys.exit()

# opencv.VideoCapture(0): Means first camera or webcam. opencv.VideoCapture(1): Means second camera or webcam. opencv.VideoCapture(“file name.mp4”): Means video file.

# 4th thing we need read our image

# this gives us two returns 1st will be true/false, if succesfully read the then it returns true else false, the 2nd is we gonna get the dimensions of image means pixel dimension
# need to store them in a two variables

res, imgDimens = img.read()

# print(res)
# print(imgDimens)
# sys.exit()

# res give us true/false
# imgDimens give us the dimension of image (pixel dimension)
# eg - let's say we have a digital image that is 1200x1800 pixels (dots). That means our digital image is 1200 dots high by 1800 dots wide.

# 5th thing we need to convert our images to greyscale images, bcoz the HaarCascade classifier is trained for greyscale images, for that we need to use CVT color method
greyScaleImg = opencv.cvtColor(imgDimens, opencv.COLOR_BGR2GRAY)
# cvtColor() is used to convert an image from one color space to another

# 6th thing we need to detect different sizes of our image
detectFaces = defineClassifier.detectMultiScale(greyScaleImg, 1.3, 5)
# it will take three parameters,
# 1 - grayscale image
# 2 - scale factor (resizing command)
# 3 - neighboring code

# print(detectFaces)
# sys.exit()

for x, y, w, h in detectFaces:
    opencv.rectangle(imgDimens, (x, y), (x + w, y + h), (255, 255, 0), 2)
    # REMEMBER it only applicable for frontal views of the faces
    # this rectangle takes 5 parameters
    # 1 - image on which we need to draw a circle
    # 2 - co-ordinates of X and Y
    # 3 - the final co-ordinates, which means the top most right hand co-ordinates
    # 4 - color of the image
    # 5 - then the width of the border


# we will get the co-ordinates of our image in detectFaces, which means x,y,width & height

# next thing show our image, not pointting co-ordinates on the faces with lines i.e face recognition
opencv.imshow("Face Recognition", imgDimens)
# it will take two parameters,
# 1 - title of our window
# 2 - the image that we want to show

# IMPORTANT NOTEE: after showing our image, everytime we need to follow three steps,
# 1 - waitkey
# 2 - release of image
# 3 - destroying of our window
opencv.waitKey(
    0
)  # if i pass 0 as params, the window opened up until we manually closes, if we 1 then its 1ms etc.
img.release()  # we need to release the captured image
opencv.destroyAllWindows()  # then im going to destroy all the windows that currently im using
