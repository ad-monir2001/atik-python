import datetime
a=datetime.datetime.now()
s=datetime.datetime.astimezone(a)
# d=datetime.datetime.today()
print(a)
print(s)
print(a.strftime('%B'))
print(a.strftime('%A'))#%a of A or w or d or b or B or m or y or Y or H or l or M or s or f or z or

print(a.strptime('',''))