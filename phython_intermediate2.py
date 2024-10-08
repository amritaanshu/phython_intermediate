# -*- coding: utf-8 -*-
"""phython_intermediate2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1il-P3M8-novxN_6gMBzSaV1Mh1aH4bqf
"""

#Tuples: ordered, immutable, allows duplicate elements
mytuple = tuple(("Max", 28, "Boston"))
print(mytuple)

for x in mytuple:
  print(x)

if "Max" in mytuple:
  print("Yes")
else:
  print("No")

#Tuple: ordered, immutable, allows duplicate elements
my_tuple = ('a', 'p', 'p', 'l', 'e')

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[:6]
print(b)

my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple2 = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple2

print(i1)
print(i2)
print(i3)

import timeit
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))