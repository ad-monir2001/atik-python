from dis import show_code
from tkinter import *
E=Entry
L=Label
Name_lab=L(text='Enter your Name:',font=('',20),width=17,height=1,background='green',foreground='cyan')
Pass_Lab=L(text='Enter your PassWord:',font=('',20),height=1,width=17,background='red',foreground='black')
Name_lab.grid(row=0,column=0)
Pass_Lab.grid(row=1,column=2)
Name_ent=E(font=('',20),foreground='cyan',width=25,)
Pass_ent=E(font=('',20,),width=25,foreground='cyan',show='*')
Name_ent.grid(row=0,column=1)
Pass_ent.grid(row=1,column=3)

Email_lab=L(text='Enter your Email:',font=('',20),width=17,height=1,background='green',foreground='cyan')
INro_lab=L(text='Your Country Name :',font=('',20),height=1,width=17,background='green',foreground='cyan')
Email_lab.grid(row=1,column=0)
INro_lab.grid(row=2,column=0)
Email_ent=E(font=('',20),foreground='cyan',width=25,)
INro_ent=E(font=('',20,),width=25,foreground='cyan',  )
Email_ent.grid(row=1,column=1)
INro_ent.grid(row=2,column=1)

mainloop()

