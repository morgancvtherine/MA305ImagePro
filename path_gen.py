from turtle import *
import math as m
hideturtle()

# Original Spiral Path Values
l = 9
theta = 0
phi = 10
d_theta = 0.05
# ---------------------------

pi = 3.141592653589793238462643383

def spiral(l, theta, stop_theta, d_theta):
    r = 0
    while theta < stop_theta:
        r = l * m.cos(theta * pi / 180) # r = l * cos(theta)
        left(theta)
        forward(r)
        theta += d_theta

spiral(l, theta, phi, d_theta)

done()