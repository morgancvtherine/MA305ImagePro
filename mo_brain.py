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
    match = cv.matchTemplate(images[1], templates[1], cv.TM_CCOEFF_NORMED)
    yes = False
    if match[0][0] > .9: 
        yes = True 
    
    return yes 