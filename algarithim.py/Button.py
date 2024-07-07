
from tkinter import *
import random
p=(random.randint(0,4))
root=Tk()
Name=Label(text='',font=('',20),width=80,height=8)
for i in range(4):
    Name.grid(row=i,column=0)
def Callback():
    global Name

    di={"Name":'Atikur Rahman',
        'Age':17,
        'Village':'Chotochapra',
        'country':'Bangladesh',
        'school':"KG"}
    l=['Name','Age','Village','country','school']

    for e in l:
        Name.configure(text=di[l[p]])
Button1=Button(text='Click here',font=("",18),background="white",foreground='green',command=Callback,)
Button1.grid(row=0,column=0)
mainloop()

