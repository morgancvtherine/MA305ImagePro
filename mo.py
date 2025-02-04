"""
M. Catherine Yopp - 6 April 2022
MA 305 - Image Processing Final 

This class is how we know how far the robot has gone 
and can visialize the path it is actually taking. This 
is the emulation of a line following robot dispite 
the lack of a physical robot. 

"""

import random as ran 
from CapnCom import CapnCom
import turtle as tu
import time as t 

#Creating Mo and the ship physically 
tu.setup(852, 480)
tu.bgpic("other_ship.gif")
tu.Screen().addshape('mo2.gif')
tu.shape('mo2.gif')
tu.hideturtle()
tu.up()
tu.setpos(x = -400, y = -100)
tu.down()
tu.showturtle()
tu.color("#503630")
tu.pensize(5)
tu.speed(.75)

#initializing the image index and choice
images = [pics for pics in range(20)]
captured = ran.choice(images)
s = 0 
cc = CapnCom(captured, s)
cc.setpath()
path_end = False

while path_end != True:
    
    images.remove(cc.cap)
    if cc.compare() == True:
        path_end = cc.end()
        images = [pics for pics in range(20)]
        cc.setcap(ran.choice(images))
        s += 1
        
        #Mo's movements
        angle = cc.direction()
        if angle == 90: 
            tu.forward(10)
        elif angle >= 0 and angle < 90: 
            tu.lt(angle)
        elif angle > 90 and angle <= 180: 
            tu.rt(angle - 90)   
                
        cc.setstep(s)
        cc.setpath()
    else:
        cc.setcap(ran.choice(images))
        cc.setpath()

t.sleep(2)
tu.clear()
tu.hideturtle()
tu.up()
tu.setpos(x = 0, y = -25)
tu.down()
tu.showturtle()
tu.color("Grey")
tu.write("Mo has cleaned the ship!", move = False, align = "center", font = ("Courier", 36, "bold"))

tu.done()
