# from sys import displayhook
# from tkinter import *
# font=Tk()

# a=Label(text='',width=10)
# a.grid(row=0,column=8)

# res_msg_str=StringVar()
# font=('',30)
# msg1=Label(text='সমান্তর ',font=font,background='white',foreground='green',)
# msg1_1=Label(text='SERIES',font=font,background='white',foreground='green')
# msg2=Label(text='গুণোত্তর ',font=font,foreground='green',background='white')
# msg2_1=Label(text='SERIES',font=font,background='white',foreground='green')
# msg1.grid(row=0,column=0)
# msg1_1.grid(row=0,column=1)
# msg2.grid(row=0,column=4)
# msg2_1.grid(row=0,column=5)
# first_letter=Label(text='first number ',font=('',20),width=10,background='cyan',foreground='black')
# difference=Label(text='difference ',font=('',20),width=10,background='lightskyblue',foreground='black')
# Nth_number=Label(text='n ',font=('',20),width=10,background='lightblue',foreground='black')
# first_letter.grid(row=1,column=0)
# difference.grid(row=2,column=0)
# Nth_number.grid(row=3,column=0)

# first_entry=Entry(font=('',20),width=10,background='white',foreground='blue')
# difference_entry=Entry(font=('',20),width=10,background='white',foreground='blue')
# Nth_entry=Entry(font=('',20),width=10,background='white',foreground='blue')
# first_entry.grid(row=1,column=1)
# difference_entry.grid(row=2,column=1)
# Nth_entry.grid(row=3,column=1)

# def call():
#     a=int(first_entry.get())
#     n=int(Nth_entry.get())
#     d=int(difference_entry.get())
#     res=int(n/2)*((2*a+((n-1)*d)))

#     res_msg_str.set('Sum({})={}'.format(n,res))
# calc_res_button=Button(text='Sumation',font=('',21),background='tan',foreground='black',width=10,command=call)
# calc_res_button.grid(row=5,column=1)
# def call1():
#     a1=int(first_entry.get())
#     s=int(Nth_entry.get())
#     d1=int(difference_entry.get())
#     res1=a1+(s-1)*d1
#     res_msg_str.set('Nth num = {}'.format(res1))
# calc_res_button=Button(text='Nth num',font=('',21),background='tan',foreground='black',width=10,command=call1)
# calc_res_button.grid(row=6,column=1)

# res_mgs_leb=Label(font=('',20),textvariable=res_msg_str,background='tan',foreground='red',width=10,height=2)
# res_mgs_leb.grid(row=7,column=1,)


# res_msg_str8=StringVar()
# font=('',30)
# first_letter1=Label(text='first number ',font=('',20),width=10,background='cyan',foreground='black')
# ratio=Label(text='ratio',font=('',20),width=10,background='lightskyblue',foreground='black')
# n1=Label(text='n',font=('',20),width=10,background='lightblue',foreground='black')
# first_letter1.grid(row=1,column=4)
# ratio.grid(row=2,column=4)
# n1.grid(row=3,column=4)

# first_entry5=Entry(font=('',20),width=10,background='white',foreground='blue')
# ratio_entry1=Entry(font=('',20),width=10,background='white',foreground='blue')
# n_entry=Entry(font=('',20),width=10,background='white',foreground='blue')
# first_entry5.grid(row=1,column=5)
# ratio_entry1.grid(row=2,column=5)
# n_entry.grid(row=3,column=5)

# def call2():
#     a8=int(first_entry5.get())
#     n3=int(n_entry.get())
#     r1=int(ratio_entry1.get())
#     res=0
#     r2=1
#     for i in range(1,n3+1):
#         res1=a8*r2
#         res=res+res1
#         r2=r2*r1
#     res9=res
#     res_msg_str8.set('Sum({})= {}'.format(n3,res9))
# def call3():
#     a3=int(first_entry5.get())
#     n4=int(n_entry.get())
#     r=int(ratio_entry1.get())
#     res3=a3*r**(n4-1)
#     res_msg_str8.set('Nth num={}'.format(res3))
    
# calc_res_button1=Button(text='Sumation',font=('',21),background='tan',foreground='black',width=10,command=call2)
# calc_res_button2=Button(text='Nth num',font=('',21),background='tan',foreground='black',width=10,command=call3)
# calc_res_button2.grid(row=6,column=5)
# calc_res_button1.grid(row=5,column=5)
# res_mgs_leb=Label(font=('',20),textvariable=res_msg_str8,background='tan',foreground='red',width=10,height=2)
# res_mgs_leb.grid(row=7,column=5,)


# mainloop()
