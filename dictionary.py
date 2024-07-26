



user={
    "user1":{
        "Name":"Atikur Rahman",
        "Gander":"Male",
        "Date of birth":"30-05-2007",
        "is married":None,

        "Area":{
                "Country":"Bangladesh",
                "District":"Bogura",
                "Village":"cotochapra"
                },
        "password":263964,
    },
    "user2":{
        "Name":"Virat Kohli",
        "Gander":"Male",
        "Date of birth":"10-11-195",
        "is married":True,
        "Area":{
                "Country":"India",
                "District":"Bangalaru",
                "Village":"vid"
        }
    },
    "user3":{
        "Name":"Babar Azam",
        "Gander":"Male",
        "Date of birth":"01-08-1992",
        "Area":{
                "Country":"Pakistan",
                "District":"United islamabad",
                "Village":"Kua"
        }
    }
}



# import json


# with open ("a.json",'w') as r:
#     r.write(json.dumps(user,indent=2,separators=(" , ",":")))

# import argparse

# parser=argparse.ArgumentParser(description="Counting")
# parser.add_argument('num1',help="Number1",type=float)
# parser.add_argument('num2',help="Number2",type=float)
# parser.add_argument('operation',default='+')
# args=parser.parse_args()
# for _ in range(2):
#     print()
# print(args)

# res=None
# if args.operation =="+":
#     res=args.num1+args.num2
    
# if args.operation =="-":
#     res=args.num1-args.num2
    
# if args.operation =="*":
#     res=args.num1*args.num2
    
# if args.operation =="**":
#     res=args.num1**args.num2
    
# print(f"result of num1 {args.operation} num2 = ",res)

# for _ in range(2):
#     print()
a8=3
r1=3
n3=2
print(f'Summation = {(a8*((r1**n3)-1))/(r1-1)}')
import re