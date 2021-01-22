#Richard markus tins
#22.01.21
from tkinter import *

def save_kontakt(nimi="nimi",num=0):
    kontakt=open("kontaktid.txt","a+")
    kontakt.write(nimi+","+num+"\n")
    return

def get_entries():
    name=entry1.get()
    num=str(entry2.get())
    save_kontakt(name,num)
    lorem3.config(text="salvestatud\n kontaktid.txt")
    return

master = Tk()
master.title('kontaktid')
master.geometry("300x150")
master.resizable(0, 0)

#nimi
lorem1 = Label(master, text="Nimi: ", font="Tahoma 12",anchor=W)
lorem1.grid(row=0,column=0)
entry1 = Entry(master)
entry1.grid(row=0, column=1)

#number
lorem2 = Label(master, text="Number: ", font="Tahoma 12",anchor=W)
lorem2.grid(row=1,column=0)
entry2 = Entry(master)
entry2.grid(row=1, column=1)

#vastus
lorem3 = Label(master, text="   ", font="Tahoma 12", fg="#fc0303",anchor=W)
lorem3.grid(row=4,column=0)

#nupp
nupp1 = Button(master, text="OK",height=1,width=7,command=get_entries)
nupp1.grid(row=2, column=1)


master.mainloop()