
('10\t0125'.expandtabs(10))

# t.write("Atikur",align="center",font=("",150,""))
# t.color('#%06x' % random.randint(0, 2**24 - 1))

# class Default(dict):
#     def __missing__(self, ke):
#         return ke

# print('{a} is born {year}'.format_map(Default()))


# import re

# def capitalize(s):
#     return re.sub(r"[A-Za-z]+",
#                   lambda mo: mo.group(0).capitalize(),
#                   s)

# print(capitalize("i am atikur rahman ."))

# print("-42".zfill(9))






# import re
# s='   Atikur     Rahman  '
# print(s.strip(''))
# print('www.example.com'.strip('cowm.'))


# print('%(language)s has %(number)03d quote types.' %
#       {'language': "Python", "number": 2})

# b'read this sort text'.translate(None,b'aeiou')


# import array
# print(array.array('f',[5,5]))
# a=array.array('l',[-1111111,2222222,-33333333,5555,99999])
# c=array.array('b',[5,3,1])
# print(memoryview(a)[0])
# v=memoryview(b'atikur')
# m=memoryview(a)
# n=memoryview(c)
# print(n.tolist()==a.tolist())

# import struct
# b=struct.pack('i'*12, *list(range(12)))
# x=memoryview(b)
# y=x.cast('L'or'i',shape=[2,2,3])
# print(x.tolist())
# [0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 7, 0, 0, 0, 8, 0, 0, 0, 9, 0, 0, 0, 10, 0, 0, 0, 11, 0, 0, 0]
# print(y.tolist())
# [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
# b=struct.pack('L'*12,*list(range(12)))
# x=memoryview(b)
# y=x.cast('L',shape=[1,2,6])


# print(bin(int()))


# def b(self):
#     s=bin(self)
#     s=s.strip('-0b')
#     return s
# b(int())


# l=[[]]*6
# l=[[] for i in range(5)]


# async def echo_round() ->[int, float]:
#     sent = yield 0
#     while sent >= 0.0:
#         rounded = await round(sent)
#         sent = yield rounded

#         yield sent
# print((echo_round()))

# '{:,}'.format(1234567890)
# '{:<30}'.format('left aligned')
# 'left aligned                  '
# '{:>30}'.format('right aligned')
# '                 right aligned'
# '{:^30}'.format('centered')
# '           centered           '
# '{:*^30}'.format('centered')  # use '*' as a fill char
# '***********centered***********'