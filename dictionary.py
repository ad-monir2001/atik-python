#DICt
# user={
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
 

user={
    "user1":{
        "Name":"Atikur Rahman",
        "Gander":"Male",
        "Date of birth":"30-05-2007",
        "Area":{
                "Country":"Bangladesh",
                "District":"Bogura",
                "Village":"cotochapra"
                }

    },
    "user2":{
        "Name":"Virat Kohli",
        "Gander":"Male",
        "Date of birth":"10-11-195",
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

a=input("Enter Area/Name/Gander/Date of birth : ")
if a=="Area":
    s=user[input("Enter any name user1/user2/user3 : ")][a]
    for key,value in s.items():
        print(f"{key}:{value}")


elif a=="Name":
    print(user[input("Enter any name user1/user2/user3 : ")][a])
elif a=="Gander":
    print(user[input("Enter any name user1/user2/user3 : ")][a])
else:
    print(user[input("Enter any name user1/user2/user3 : ")][a])
