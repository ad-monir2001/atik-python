#DICt
user={
    "Name":"Atikur",
    "age":17,
    "gender":"male",
    "IS_maried":False,
    "hobbies":["reading","playing","programming"],
    "c":{"country":"Bangladesh",
        "city":"Bogura",
        "village":"chotochapra"}
    }

for a,b in user.items():
    print(f"{a}:{b}")

user["Name"]="Rahman"
print(user)
print(user.get("Name"))