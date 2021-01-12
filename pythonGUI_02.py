#Richard markus tins
#12.01.21
import turtle

#ekraan
a=turtle.Screen()
a.setup(300,300)
a.bgcolor("black")

def star(x=5):
    turtle.color("blue")
    turtle.speed(10)
    for i in range(x):
        turtle.fd(100)
        turtle.rt(-144)

def triangle(a=100,cr="red"):
    turtle.color(cr)
    for i in range(3):
        turtle.fd(a)
        turtle.lt(120)
        

star()
triangle(100,"white")

