import random as ran 
from CapnCom import CapnCom
"""
M. Catherine Yopp
MA 305 - Image Processing Final 

This script is how the robot will "move"

"""
images = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
captured = ran.choice(images)
s = 0 

cc = CapnCom(captured, s)
cc.setpath()


path_end = False 

while path_end != True:
    
    images.remove(cc.cap)
    if cc.compare() == True:
        path_end = cc.end()
        print(cc.cap)
        images = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        cc.setcap(ran.choice(images))
        #This is where the gui would be placed using cc.direction()
        
        s += 1
        cc.setstep(s)
        cc.setpath()
    else:
        cc.setcap(ran.choice(images))
        cc.setpath()
                
print("Mo has cleaned all of Wall-E's tracks!")
