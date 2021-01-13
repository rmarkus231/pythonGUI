#Richard markus tins
#13.01.21
import turtle
import time

#ekraan
a=turtle.Screen()
a.setup(500,400)
a.bgcolor("black")
turtle.speed(100)

#soojendus
def square(a):
    turtle.color("white")
    turtle.rt(a)
    for i in range(4):
        turtle.fd(50)
        turtle.rt(90)
        
#ül nr 9
def kujund1():
    k=turtle.Turtle()
    k.color("white")
    for i in range(4):
        k.right(90*i)
        for i in range(4):
            k.fd(30)
            k.rt(90)
            k.fd(30)
            k.lt(90)
            k.fd(30)
            k.lt(90)

#ül nr 11
def kolmnurk():
    k=turtle.Turtle()
    k.color("white")
    k.speed(10)
    for i in range(10):
        k.rt(45)
        for i in range(3):
            k.fd(50)
            k.lt(120)

#ül nr7
def kujund2():

    k=turtle.Turtle()
    k.color("white")
    for i in range(8):
        k.lt(90)
        for j in range(2):
            k.fd(50)
            k.rt(90)
            k.fd(25)
            k.rt(90*(j+1))
        k.fd(25)
        k.rt(45)

#square(-69)

#kujund1()

#kolmnurk()

kujund2()


turtle.exitonclick()
