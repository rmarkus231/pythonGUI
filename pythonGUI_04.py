#Richard markus tins
#18.01.21
from tkinter import *

#akna seaded
aken = Tk()
aken.title('Kalkulaator')
aken.geometry("200x200")
aken.resizable(0, 0)

#text
lorem = Label(aken, text="Siia kunagi vastus!", font="Tahoma 12")
lorem.grid(row=0,column=0, columnspan=4, sticky=E+W)

#nupud 1 rida
nupp1 = Button(aken, text="7",height=2,width=4)
nupp1.grid(row=2, column=0, padx=2)
nupp2 = Button(aken, text="8",height=2,width=4)
nupp2.grid(row=2, column=1, padx=2)
nupp3 = Button(aken, text="9",height=2,width=4)
nupp3.grid(row=2, column=2,padx=2)
nupp4 = Button(aken, text="/",height=2,width=4)
nupp4.grid(row=2, column=3,padx=2)

#nuppud 2 rida
nupp5 = Button(aken, text="4",height=2,width=4)
nupp5.grid(row=3, column=0, padx=2)
nupp6 = Button(aken, text="5",height=2,width=4)
nupp6.grid(row=3, column=1, padx=2)
nupp7 = Button(aken, text="6",height=2,width=4)
nupp7.grid(row=3, column=2,padx=2)
nupp8 = Button(aken, text="*",height=2,width=4)
nupp8.grid(row=3, column=3,padx=2)

#nuppud 3 rida
nupp9 = Button(aken, text="1",height=2,width=4)
nupp9.grid(row=4, column=0, padx=2)
nupp10 = Button(aken, text="2",height=2,width=4)
nupp10.grid(row=4, column=1, padx=2)
nupp11 = Button(aken, text="3",height=2,width=4)
nupp11.grid(row=4, column=2,padx=2)
nupp12= Button(aken, text="-",height=2,width=4)
nupp12.grid(row=4, column=3,padx=2)

#nuppud 4 rida
nupp13 = Button(aken, text="0",height=2,width=4)
nupp13.grid(row=5, column=0, padx=2)
nupp14 = Button(aken, text=",",height=2,width=4)
nupp14.grid(row=5, column=1, padx=2)
nupp15 = Button(aken, text="=",height=2,width=4)
nupp15.grid(row=5, column=2,padx=2)
nupp16 = Button(aken, text="+",height=2,width=4)
nupp16.grid(row=5, column=3,padx=2)

aken.mainloop()
