#Richard markus tins
#18.01.21
from tkinter import *

master = Tk()
master.title('Tšehhi')
master.geometry("300x450")
master.resizable(0, 0)

#canvas
canvas=Canvas(master, width=300,height=450)

canvas.create_rectangle(0,200,300,100,fill="#990000",outline="#990000")
canvas.create_rectangle(0,100,300,0,fill="white",outline="white")
canvas.create_polygon(0,0,0,200,150,100,fill="#3366ff",outline="#3366ff")

canvas.create_line(0,200,300,200,fill="black",width=2)

#pilt
pilt=PhotoImage(file='tšehhi.png')
canvas.create_image(0,230,anchor=NW,image=pilt)

canvas.pack()
master.mainloop()