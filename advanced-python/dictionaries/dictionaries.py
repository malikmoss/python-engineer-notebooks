
mydict = {"name":"Malik", "age": 30, "city": 'Houston'}

# mydict2 = dict(name="Malik", age=30, city="Houston")
# print(mydict2)

mydict["email"] = "em@il"

# del mydict["email"]

# mydict.popitem()
# print(mydict)

# if "name" in mydict:
#     print(mydict["name"])

# if "lastname" in mydict:
#     print(mydict["lastname"])

# or

# try:
#     print(mydict["name"])
# except:
#     print("Error")

#loop through dictionary
# for keyers in mydict.keys():
#     print(keyers)

# for values in mydict.values():
#     print(values)

# for key,value in mydict.items():
#     print(key,value)

#copying dictionaries
#modifying copies will also modify the original unlees you use copy() or dict function
# mydict_copy = mydict.copy()
# mydict_copy = dict(mydict)
# mydict_copy["email"] = "moss@govalo"

# print(mydict)
# print(mydict_copy)