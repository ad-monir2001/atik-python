 #! # DICt
#user={
#     "Name":"Atikur",
#     "age":17,
#     "gender":"male",
#     "IS_maried":False,
#     "hobbies":["reading","playing","programming"],
#     "c":{"country":"Bangladesh",
#         "city":"Bogura",
#         "village":"chotochapra"}
#     }

# for a,b in user.items():
#     print(f"{a}:{b}")

# user["Name"]="Rahman"
# print(user)
# print(user.get("Name"))
 



# user={
#     "user1":{
#         "Name":"Atikur Rahman",
#         "Gander":"Male",
#         "Date of birth":"30-05-2007",
#         "Area":{
#                 "Country":"Bangladesh",
#                 "District":"Bogura",
#                 "Village":"cotochapra"
#                 }
#     },
#     "user2":{
#         "Name":"Virat Kohli",
#         "Gander":"Male",
#         "Date of birth":"10-11-195",
#         "Area":{
#                 "Country":"India",
#                 "District":"Bangalaru",
#                 "Village":"vid"
#         }
#     },
#     "user3":{
#         "Name":"Babar Azam",
#         "Gander":"Male",
#         "Date of birth":"01-08-1992",
#         "Area":{
#                 "Country":"Pakistan",
#                 "District":"United islamabad",
#                 "Village":"Kua"
#         }
#     }
# }
# while True:
#     #=======================================
#     choose=[ "users sort information","users full information"]
#     c=input(f"please choose anything,, {choose[0]}/{choose[1]} : ")
#     #=======================================
#     if c==f'{c}':
#         u=input("Enter any user user1/user2/user3 : ")
#         a=input("Enter Area/Name/Gander/Date of birth : ")
#         if a.capitalize()=="Area":
#             s=user[u][a.capitalize()]
#             for key,value in s.items():
#                 print(f"{key}:{value}")
#         elif a.capitalize()=="Name"or"Gander"or"Date of birth":
#             print(user[u][a.capitalize()])
#     #=======================================
#     else:
#         for k,v in user[input("Enter any user user1/user2/user3 : ")].items():
#             print(f'{k}:{v}')

#     us=list(map(str,input("which village do you want to see ? :").split(" ")))
#     for i in us:
#         if i in user:
#             print(user[i]["Area"]["Village"])
#         else:
#             break


# O/x puzzle game

while True:
    def count(x):

        try:
            return 0/x
        except ZeroDivisionError as a:
            print(a)


        except TypeError as m:
            print(m)
        except ValueError as e :
            print(e)
        finally :
            print(0/x)

    print(count(int(input())))



def mu(x):
    try:
        return 0/x
    except ZeroDivisionError as z : 
        print("yor are win the game ")


print(mu(int(input())))
