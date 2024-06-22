



# from tkinter import Label


# for i in range(16):
#     l=Label(text=str(i),font=('Verdana',16))
#     (l.grid(row=1//4 , column=i%4))
#     Label.append(l)

# from tkinter import Button, Label, Tk


# root=Tk()
# font='Verdana',16
# clicked_label=Label(text='Not clicked',font=font,width=25)
# clicked_label.grid(row=0 , column= 0)
# def callback():
#     clicked_label.configure(text='Button was clicked')
    

# clicker_button=Button(text='click here',font=font,width=12,command=callback)
# (clicker_button.grid(row=10,column=0))
# (callback())


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        res=list(set(nums))
        res.sort(reverse=True)


        if len(res)>=3:
            return res[2]
        if len(res)<3:
            return max(res)

s=Solution()
print(s.thirdMax([-1,2,3]))
print(s.thirdMax([3,2,1,7,5,8]))


a=[-1,2,3]
a.sort()
print(a)

