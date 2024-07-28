from tkinter import *
from tkinter import ttk
t=Tk()
frame=Frame(t)
frame.pack()

value=['Python','Java',"PHP",'C','C++','JavaScript','Python3','TypeScript','Scala','Kotlin']
comb=ttk.Combobox(frame,values=value,font=('',15),background='white',foreground='green')
comb.set('take an option',)
comb.pack(padx=100,pady=20)



mainloop()




# from tkinter import *

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# mylist = Listbox(root, yscrollcommand=scrollbar.set)

# for line in range(100):
#     mylist.insert(END, 'This is line number' + str(line))
    
# mylist.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
# mainloop()


# from tkinter import *

# master = Tk()
# w = Scale(master, from_=0, to=42)
# w.pack()
# w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w.pack()
# mainloop()

# from tkinter import *

# master = Tk()
# w = Spinbox(master, from_=0, to=10)
# w.pack()
# mainloop()


