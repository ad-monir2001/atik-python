
from tkinter import *


font=Tk()

a=Label(text='',width=10)
a.grid(row=0,column=8)

res_msg_str=StringVar()
res_msg_str0=StringVar()
res_msg_str1=StringVar()
res_msg_str2=StringVar()
res_msg_str3=StringVar()
font=('',30)
msg1=Label(text='সমান্তর ',font=font,background='white',foreground='green',)
msg1_1=Label(text='ধারা OR SERIES',font=font,background='white',foreground='green')
msg2=Label(text='গুণোত্তর ',font=font,foreground='green',background='white')
msg2_1=Label(text='ধারা OR SERIES',font=font,background='white',foreground='green')
msg1.grid(row=0,column=0)
msg1_1.grid(row=0,column=1)
msg2.grid(row=0,column=4)
msg2_1.grid(row=0,column=5)
first_letter=Label(text='first number ',font=('',20),width=10,background='cyan',foreground='black')
difference=Label(text='difference ',font=('',20),width=10,background='lightskyblue',foreground='black')
Nth_number=Label(text='n ',font=('',20),width=10,background='lightblue',foreground='black')
first_letter.grid(row=1,column=0)
difference.grid(row=2,column=0)
Nth_number.grid(row=3,column=0)

first_entry=Entry(font=('',20),width=20,background='white',foreground='blue')
difference_entry=Entry(font=('',20),width=20,background='white',foreground='blue')
Nth_entry=Entry(font=('',20),width=20,background='white',foreground='blue')
first_entry.grid(row=1,column=1)
difference_entry.grid(row=2,column=1)
Nth_entry.grid(row=3,column=1)
class SERIES:
    def __init__ (self,):
        a=int(first_entry.get())
        n=int(Nth_entry.get())
        d=int(difference_entry.get())
        li=[f'Summation({n}) = n/2.(2a+(n-1)d)',f'summation({n})={n}/2.(2.{a}+({n}-1).{d})',f'...Summation({n}).={n}/2.({a*2}+({(n-1)*d}))',f'NOW..Summation({n}). = {n}/2.({a*2+(n-1)*d})',f'So,the summation({n})= {(n/2)*(2*a+(n-1)*d)}']
        res_msg_str.set('{}'.format(li[0]))
        res_msg_str0.set('{}'.format(li[1]))
        res_msg_str1.set('{}'.format(li[2]))
        res_msg_str2.set('{}'.format(li[3]))
        res_msg_str3.set('{}'.format(li[4]))

calc_res_button=Button(text='Sumation',font=('',20),background='tan',foreground='black',width=18,command=SERIES.__call__)
calc_res_button.grid(row=5,column=1)
def call1():
    a1=int(first_entry.get())
    s=int(Nth_entry.get())
    d1=int(difference_entry.get())
    N_li=['Nth num = a + (n-1).d',
    f'Nth num = {a1} + ({s}-1).{d1}',
    f'Nth num = {a1} + ({s-1}).{d1}',
    f'now,Nth num = {a1} + ({(s-1)*d1})',
    f'So the Nth num = {a1 + (s-1)*d1}']
    res_msg_str.set('{}'.format(N_li[0]))
    res_msg_str0.set('{}'.format(N_li[1]))
    res_msg_str1.set('{}'.format(N_li[2]))
    res_msg_str2.set('{}'.format(N_li[3]))
    res_msg_str3.set('{}'.format(N_li[4]))
    
    
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=7,column=1,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str0,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=8,column=1,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str1,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=9,column=1,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str2,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=10,column=1,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str3,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=11,column=1,)
calc_res_button=Button(text='Nth num',font=('',20),background='tan',foreground='black',width=18,command=call1)
calc_res_button.grid(row=6,column=1)


res_msg_str4=StringVar()
res_msg_str5=StringVar()
res_msg_str6=StringVar()
res_msg_str7=StringVar()
res_msg_str8=StringVar()

font=('',30)
first_letter1=Label(text='first number ',font=('',20),width=10,background='cyan',foreground='black')
ratio=Label(text='ratio',font=('',20),width=10,background='lightskyblue',foreground='black')
n1=Label(text='n',font=('',20),width=10,background='lightblue',foreground='black')
first_letter1.grid(row=1,column=4)
ratio.grid(row=2,column=4)
n1.grid(row=3,column=4)

first_entry5=Entry(font=('',20),width=20,background='white',foreground='blue')
ratio_entry1=Entry(font=('',20),width=20,background='white',foreground='blue')
n_entry=Entry(font=('',20),width=20,background='white',foreground='blue')
first_entry5.grid(row=1,column=5)
ratio_entry1.grid(row=2,column=5)
n_entry.grid(row=3,column=5)

def call2():
    a8=int(first_entry5.get())
    n3=int(n_entry.get())
    r1=int(ratio_entry1.get())
    li_g=['Summation = a.(r^(n)-1)/r-1',
    f'Summation = {a8}.({r1}^{n3}-1)/{r1}-1',
    f'Summation = {a8}.({r1**n3}-1)/{r1-1}',
    f'Summation = {a8}.({(r1**n3)-1})/{r1-1}',
    f'Summation = {(a8*((r1**n3)-1))/(r1-1)}']
    res_msg_str4.set('{}'.format(li_g[0]))
    res_msg_str5.set('{}'.format(li_g[1]))
    res_msg_str6.set('{}'.format(li_g[2]))
    res_msg_str7.set('{}'.format(li_g[3]))
    res_msg_str8.set('{}'.format(li_g[4]))

def call3():
    a3=int(first_entry5.get())
    n4=int(n_entry.get())
    r=int(ratio_entry1.get())
    li_g_n=['or,Nth num = a.r^(n-1)',
    f'or,Nth num = {a3}.{r}^({n4}-1)',
    f'or,Nth num = {a3}.{r}^({n4-1})',
    f'or,Nth num = {a3}.{r**(n4-1)}',
    f'So the Nth num = {a3*r**(n4-1)}']
    res_msg_str4.set('{}'.format(li_g_n[0]))
    res_msg_str5.set('{}'.format(li_g_n[1]))
    res_msg_str6.set('{}'.format(li_g_n[2]))
    res_msg_str7.set('{}'.format(li_g_n[3]))
    res_msg_str8.set('{}'.format(li_g_n[4]))

res_mgs_leb=Label(font=('',15),textvariable=res_msg_str4,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=7,column=5,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str5,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=8,column=5,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str6,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=9,column=5,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str7,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=10,column=5,)
res_mgs_leb=Label(font=('',15),textvariable=res_msg_str8,background='tan',foreground='black',width=26,height=2)
res_mgs_leb.grid(row=11,column=5,)
calc_res_button1=Button(text='Sumation',font=('',21),background='tan',foreground='black',width=18,command=call2)
calc_res_button2=Button(text='Nth num',font=('',21),background='tan',foreground='black',width=18,command=call3)
calc_res_button2.grid(row=6,column=5)
calc_res_button1.grid(row=5,column=5)

mainloop()


