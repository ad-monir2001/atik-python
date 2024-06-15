dictionaries=[
    {'name':'Atikur','house':'cotochapra','age':17},
    {'name':'shoel','house':'faridpur','age':17.5},
    {'name':'shakib','house':'magura','age':32},
    {'name':None,'house':False,'age':True}
]
for dictionary in dictionaries:
    for dict in dictionary:
        print(dict,dictionary[dict],sep=':')
        
a=0   
while a<3:
    a=a+1
    for key,values in dictionaries[a].items():
        print(key , values,sep=':')
        
