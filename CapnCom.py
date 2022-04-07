"""
M. Catherine Yopp - 6 April 2022
MA 305 - Image Processing Final 

This is where the predetermined path is established and how 
the robot knows what images to compare and which image is 
"captured". 
"""
import mo_brain as brain 

class CapnCom: 
    
    def __init__(self, captured_image, step):
        
        self.cap = captured_image 
        self.step = step
        self.path = 9
        
    def setcap(self, captured_image):
        self.cap = captured_image
        
    def setstep(self, step):
        self.step = step
      
    def setpath(self):
               
        if  self.step == 5:
            self.path = 1
        elif self.step == 10:
            self.path = 2    
        elif self.step == 15:
            self.path = 3
        elif self.step == 25:
            self.path = 14
        elif self.step == 30:
            self.path = 13
        elif self.step == 35:
            self.path = 10
        elif self.step == 45:
            self.path = 2
        elif self.step == 55:
            self.path = 1
        elif self.step == 75:
            self.path = 3
        elif self.step == 85:
            self.path = 1
        elif self.step == 95:
            self.path = 4
        elif self.step == 105:
            self.path = 19 
        else: 
            self.path = 9
       
    def direction(self):    
     angle = self.path * 10     
     
     return angle 

    def compare(self):          
        same = False
        same = brain.match(self.cap, self.path)
         
        return same 
    
    def end(self): #for 20th image: replace the passed function to angle 
        end = False 
        if self.path == 19 and self.compare() == True : #for 20th image: angle == 'NULL"
            end = True
               
        return end 
        

