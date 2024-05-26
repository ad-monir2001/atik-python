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
# choose=[ "users sort information","users full information"]
# c=input(f"please choose . {choose[0]}  or  {choose[1]} : ")


# if c==choose[0]:
#     u=input("Enter any user user1/user2/user3 : ")
#     a=input("Enter Area/Name/Gander/Date of birth : ")
#     if a.capitalize()=="Area":
#         s=user[u][a.capitalize()]
#         for key,value in s.items():
#             print(f"{key}:{value}")
#     elif a.capitalize()=="Name"or"Gander"or"Date of birth":
#         print(user[u][a.capitalize()])


# else:
#     for k,v in user[input("Enter any user user1/user2/user3 : ")].items():
#         print(f'{k}:{v}')

country={ 

  "Barisal":{
      "Barguna","Barisal","Bhola","Jhalokati","Patuakhali", "Pirojpur"
      },

  "Chittagong":{
      "Bandarban","Brahmanbaria","Chandpur","Chittagong","Comilla","Cox's Bazar","Feni","Khagrachhari","Lakshmipur", "Noakhali","Rangamati"
                },

  "Dhaka":{
      "Dhaka","Faridpur","Gazipur","Gopalganj","Kishoreganj","Madaripur","Manikganj","Munshiganj","Rajbari","Narayanganj","Narsingdi","Tangail","Shariatpur"
      },

  "Khulna":{
      "Bagerhat", "Chuadanga","Jessore","Jhenaidah","Khulna",     "Kushtia","Magura","Meherpur",    "Narail","Satkhira"
      },

  "Mymensingh":{
      "Jamalpur", "Mymensingh","Netrakona","Sherpur"
      },

  "Rajshahi":{
        "Bogra":{
          "Bogura sadar","sherpur","dhunat","Sariakandi",
            },
        "Chapainawabganj":{},"Joypurhat":{},"Naogaon":{},"Natore":{},"Pabna":{},"Rajshahi":{},"Sirajganj":{}
        },

  "Rangpur":{"Dinajpur", "Gaibandha","Kurigram", "Lalmonirhat","Nilphamari","Panchagarh","Rangpur","Thakurgaon"},

  "Sylhet":{"Habiganj","Moulvibazar","Sunamganj","Sylhet"}

}
for k,v in country["Rajshahi"].items():
    print(f"{k}:{v}")