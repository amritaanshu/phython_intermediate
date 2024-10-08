# -*- coding: utf-8 -*-
"""phython_intermediate3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16JLS4JQudzpDZshC5GuLdqsSNFSZOr_X
"""

#Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "City": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

value = mydict["age"]
print(value)

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict)

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

del mydict["name"]
print(mydict)

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

if "lastname" in mydict:
  print(mydict["lastname"])

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

try:
  print(mydict["lastname"])
except:
  print("Error")

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

for key in mydict:
  print(key)

for key, value in mydict.items():
  print(key, value)

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict_cpy = mydict

mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

mytuple = (8, 7)
mydict = {mytuple: 15}

print(mydict)