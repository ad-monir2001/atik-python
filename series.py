
user_choose=input('som_series or jun_series ')
if user_choose=="som_series":
    list1=[]
    inp=input('sumation or Nth ')
    if inp=="sumation":
            
        series_with_sign=input('Please give your series ')
        N=int(input('cototi poder sumation chao '))
        for i in series_with_sign:
            if i !='+' and ".":
                list1.append(int(i))
            
        D=list1[1]-list1[0]
        A=list1[0]
        Sumation=(N/2*(2*A+(N-1)*D))
else:
    pass