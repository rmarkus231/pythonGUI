#Richard markus tins
#12.01.21
import turtle
import random

#ekraan
a=turtle.Screen()
a.setup(500,300)
a.bgcolor("black")



def arrows(rt=0):
    color=["red","blue","yellow","green"]
    x=360/rt
    turtle.speed(0)
    turtle.shape("circle")
    for i in range(int(rt)):
        turtle.color(color[random.randint(0,3)])
        turtle.rt(x)
        turtle.fd(100)
        turtle.bk(100)
    return

arrows(1440)    

turtle.exitonclick()