"""
M. Catherine Yopp - 6 April 2022
MA 305 - Image Processing Final 

This class is where the robot's thinking takes place as it process 
the two images by breaking them down into arrays of the rgb values 
of each pixel and comparing those values to determine if the photos 
match one another. 

"""

import numpy as np
import cv2 as cv     
   
images = [] 
templates = []

for i in range(20):
    deg = i * 10 
    pic = "%ideg_line.png" %deg
    picture = cv.imread(pic)
    picture.astype(np.float32)
    images.append(picture)
    templates.append(picture)
    
def match(cap, path):
    yes = False
    compare = [[0],[0]]
    try:
        compare = cv.matchTemplate(images[path], templates[cap], cv.TM_CCOEFF_NORMED)
        
    except BaseException:    
        compare[0][0] = 0
        
    if compare[0][0] > .9: 
        yes = True
    
    return yes 

