from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
t=Tk()
def show():
    filename=askcolor()
    print(filename)
    
B=Button(t,text='Click',command=show)
B.place(x=50,y=50)
t.mainloop()
