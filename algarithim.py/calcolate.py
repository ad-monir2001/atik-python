from tkinter import *
font=Tk()
res_msg_str=StringVar()
font=('',30)
msg1=Label(text='if youe give me a series , I will give you the Sumation of this series.',font=font,width=55,background='white',foreground='green')
msg1.grid(row=0,column=0,columnspan=100)
first_letter=Label(text='first number ',font=('',20),width=30,background='cyan',foreground='black')
difference=Label(text='difference of 1st and 2st number',font=('',20),width=30,background='lightskyblue',foreground='black')
Nth_number=Label(text='Length of total number',font=('',20),width=30,background='lightblue',foreground='black')
first_letter.grid(row=1,column=20)
difference.grid(row=2,column=20)
Nth_number.grid(row=3,column=20)
first_entry=Entry(font=('',20),width=40,background='white',foreground='blue')
difference_entry=Entry(font=('',20),width=40,background='white',foreground='blue')
Nth_entry=Entry(font=('',20),width=40,background='white',foreground='blue')
first_entry.grid(row=1,column=21)
difference_entry.grid(row=2,column=21)
Nth_entry.grid(row=3,column=21)
def call():
    a=int(first_entry.get())
    n=int(Nth_entry.get())
    d=int(difference_entry.get())
    res=(n/2)*((2*a+((n-1)*d)))
    res_msg_str.set('The sumati of this series is {}'.format(res))
calc_res_button=Button(text='Calculate the sumation',font=('',21),background='tan',foreground='black',width=37,command=call)
calc_res_button.grid(row=4,column=21)
res_mgs_leb=Label(font=('',20),textvariable=res_msg_str,background='tan',foreground='red',width=37,height=2)
res_mgs_leb.grid(row=5,column=21,)
mainloop()