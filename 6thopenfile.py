 #!variable=open("file_Name","r")
#*print(variable.read())
#!with open("pratice.py","r"or"w+") as variable:
#*    o=(variable.readline() or write("anything")) 
#*    for a in o:
#*        print(o)
with open("r.css","w+") as a:
    # a.write("#!Int will\n't turn into list but str will turn into list.List is mutable. ")
    (a.write("A=Atikur"))
    a.seek(1)
    print(a.read())
    print(a.tell())
#write n file
# !with open ("Atikur.html","x") as p:
#  !   p.write("<!Doctype>")