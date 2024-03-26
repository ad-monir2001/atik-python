# #  #!LIST 
#!Int will\n't turn into list but str will turn into list.List is mutable. 
#! enumerate method add a key with every value of list
VARIABLE=['ATIKUR RAHMAN','RONA',"HOW"]
VARIABLE.append("ANYTHING")#**ADD AN ELEMENT TO THE END OF LHE LIST
# VARIABLE.count("ANY ELEMENTS")
# VARIABLE.insert(2,"2ARGUMENT")
# VARIABLE.remove("REMOVES ANYTHING FROM THE LIST")
#  VARIABLE.clear("REMOVES ALL ITEMS")
#  VARIABLE.reverse()
#  #!BUILT IN FUNCTION
# len(VARIABLE)#*IT RETURNS LENGTH OF THE LIST
# #sum(int(VARIABLE))#*IT RETURNS SUMS THE NUMBERS OF LIST.
# #filter(VARIABLE)
# print(list(enumerate(VARIABLE)))
print("{0} is my name".format(VARIABLE[0]))
# !TUPLES
#!TUPLES is immutable.But list is mutable .Besides,all rules of  tuples is about list.('count', 'index','max,min'__add__,__len__.__mul__)
# print(dir(tuple))
a=((3,5),(6,6),(9,6),3)
s=(3,"s","a","sd")
(a.__mul__(3))
print(a.__add__(s))#*==a+s
(a.__len__())#**==len(a)
# print(max or min(a[2]))
# a[1,3,6,5]#!Here,We can use list slicing rules. 