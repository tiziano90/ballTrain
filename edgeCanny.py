import cv2
import numpy as np
import os
import sys


check = True
while check:
    location=raw_input("Select Directory: ")
    if(os.path.isdir(location)):
        print "Directory selected: ",location
        check = False
    else:
        print "Please select a valid directory."


for filename in os.listdir(location):
    img = cv2.imread(os.path.join(location,filename))
    key = 1
    if img is not None:
    	edges = cv2.Canny(img,100,200) 	    
        output='output_edge/'+filename
        cv2.imwrite(output,edges)


