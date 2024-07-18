# print('Atikur Rahman','Atik',sep='""""')
# name=input("Nmae : ")
# first,last=name.split("   ")
# print(f'{first},{last}')

names=[]
for _ in range(3):
    names.append(input('what is your name? '))
    
    
for name in sorted(names):
    print(f'hello {name}')