#Richard markus tins
#12.01.21
from tkinter import *

#akna seaded
aken = Tk()
aken.title('Richard Markus Tins')
#aken.geometry("300x300")
aken.resizable(0, 0)

#tekst
text = 'Richard Markus Tins \nIT20\n2020'
tekst = Label(aken, text=text, wraplength=500, background="black",foreground="red", font="Tahoma 30 bold italic")
tekst.pack()

aken.mainloop()
