from turtle import *

l = 100 # line length
step = 10 # step size

def dataset(l, step):
    # Generates dataset 18 image dataset (180deg is 0deg line)
    theta = 0 # initializes theta
    for i in range(0,18):
        clearscreen()  # clears screen
        resetscreen() # resets turtle to original position
        hideturtle() # hides turtle
        left(theta) # rotates turtle theta degrees
        forward(l) # moves distance l forward
        theta += step # adds degree step to theta
        input("enter go when image is saved: ")
        # stalls program until user allows it to continue
    bye() # closes window

dataset(l, step)

done()