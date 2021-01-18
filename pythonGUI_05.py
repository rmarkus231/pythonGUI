#Richard markus tins
#18.01.21
from tkinter import *

master = Tk()
master.title('käibemaksukalkulaator')
master.geometry("300x200")
master.resizable(0, 0)

def naita_valikut():
    v= var.get()
    return v

def arvuta():
    a= entry.get()
    v=naita_valikut()
    maks=float(a)/100*float(v)
    hind=float(a) + float(maks)
    vastus1= Label(master, text=f"{round(maks,2)}€", font="Tahoma 12")
    vastus1.grid(row=4,column=1)
    vastus2= Label(master, text=f"{round(hind,2)}€", font="Tahoma 12")
    vastus2.grid(row=5,column=1)


#rida 1
lorem = Label(master, text="Hind käibemaksuta: ", font="Tahoma 12")
lorem.grid(row=0,column=0)
entry = Entry(master)
entry.grid(row=0, column=1)

#rida 2
lorem = Label(master, text="Käibemaksumäär: ", font="Tahoma 12")
lorem.grid(row=1,column=0)
#valiku nuppud
var = IntVar()
valikukast = Radiobutton(master,text="9%", variable=var, value=9)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(master,text="20%", variable=var, value=20)
valikukast.grid(row=2, column=1)

#joon
lorem = Label(master, text="-"*40 , font="Tahoma 12")
lorem.grid(row=3,columnspan=2)

#nupp


nupp1 = Button(master, text="OK",height=1,width=7, command=arvuta)
nupp1.grid(row=6, column=1)

käibemaks=0.00
hind=0.00

#rida 3,4
lorem = Label(master, text="Käibemaks: ", font="Tahoma 12")
lorem.grid(row=4,column=0)
vastus1= Label(master, text=f"{käibemaks}€", font="Tahoma 12")
vastus1.grid(row=4,column=1)

lorem = Label(master, text="Hind käibemaksuga: ", font="Tahoma 12")
lorem.grid(row=5,column=0)
vastus2= Label(master, text=f"{hind}€", font="Tahoma 12")
vastus2.grid(row=5,column=1)


master.mainloop()