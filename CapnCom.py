"""
M. Catherine Yopp
MA 305 - Image Processing Final 

This class is where the robot's thinking will take place 

"""
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
        
        #this is how we pick what the path looks like
        #below, I just made some stuff up for the sake of presentation
        #the elif statments represent 'turns' and once the robot makes the turn
        #it will be parallel to the path so after it turns, the image it will be 
        #'looking' at is the 90 degree image, which is taken care of in the else statement 
        
        if  self.step == 7:
            self.path = 15
        elif self.step ==  17:
            self.path = 13
        elif self.step == 25:
            self.path = 3
        elif self.step == 68:
            self.path = 4
        elif self.step == 95:
            self.path = 19 #This is the stopping position or 20th photo 
        else: 
            self.path = 9
       
    def direction(self):
        #this is where the numbers of the data set will also be assigned their angle value 
        #this function will be used to assist with the gui that will trace out the path as the robot moves
     angle = self.path * 10
           
     return angle 

    def compare(self): 
            
        same = False
          
        """
        This function is where the image processing will occur.
        Depending on how extensive/long the code is, it might need its own 
        class so that it can pass a boolean variable. 
        
        This function or class will have the numbers assigned to the images. 
        The self.path and self.cap variables will be used to pull two images 
        out of the dataset for the image processing comparison. From there, 
        that is how the 'same' vaiable will be set to either True or False 
        
        """
        # This is just for testing the code that this class will be 
        #imported into 
        if self.cap == self.path:                 
            same = True      
        else:
            same = False
         
        return same 
    
    def end(self): #for 20th image: replace the passed function to angle 
        end = False 
        if self.path == 19 and self.compare() == True : #for 20th image: angle == 'NULL"
            end = True
               
        return end 
        

