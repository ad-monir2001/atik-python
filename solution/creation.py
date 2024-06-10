s=[]
def convert_string_to_the_int_without_eng_l(a):
    for i in a:
        if ((i.isdigit() is  True)):
            s.append(i)
    str=(''.join(s))
    print(f'the converting value of {a} is {int(str)}')