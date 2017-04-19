

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
	if img is not None:
		edges = cv2.Canny(img,50,150,apertureSize = 3)
		minLineLength=50
		lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)
		if lines is not None:
			a,b,c = lines.shape
			for i in range(a):
			    cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.CV_AA)
			    output='output_line/'+filename
		        cv2.imwrite(output,img)
