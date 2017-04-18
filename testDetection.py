import cv2
import os

#cascade = cv2.CascadeClassifier("outputDirectory/cascade.xml")


import sys


check = True
while check:
    location=raw_input("Select Directory with images: \n")
    if(os.path.isdir(location)):
        print "Directory selected: ",location
        check = False
    else:
        print "Please select a valid directory."

check2=True
while check2:
    locationClassifier=raw_input("Select Classifier ( outputDirectory/cascade.xml ? ): \n")
    if(os.path.isdir(location)):
        print "Directory selected: ",location
        check2 = False
    else:
        print "Please select a valid directory."

cascade = cv2.CascadeClassifier(locationClassifier)
folder = "upper"
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))
    key = 1
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        balls = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(24, 24)    	    )
    # Draw a rectangle around the balls
    for (x, y, w, h) in balls:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if len(balls) > 0:  	    
        cv2.imshow('image',img)
        cv2.waitKey(0) & 0xFF
        output='output/'+filename
        #cv2.imwrite(output,img)
        cv2.destroyAllWindows()


