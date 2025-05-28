"""
File: Tuples_and_Methods_Part2.py
Author: Moataz Elhawary
Date: 2024-09-08 
"""

# -----------
# -- Tuple --
# -----------

# Tuple With One Element

myTuple1 = ("Moataz",)
myTuple2 = "Moataz",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))


# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a+b
d = a+("A", "B")+b

print(c)
print(d)


# Tuple , List , String Repeat (*)

myString = "Moataz "
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)


# Method => count()

a = (1, 2, 4, 5, 3, 2, 5, 3, 2, 1)
print(a.count(1))
print(a.count(3))

# Method => index()

b = (1, 2, 4, 5, 2, 3, 5, 3, 5)
# print ("The Position of Index Is : " + b.index(5))  # Not Valid
print("The Position of Index Is : {} " .format(b.index(5)))
print(f"The Position of Index Is : {b.index(5)} ")

# Tuple Destruct

a = ("A", "B", 4, "C")
x, y, _, z = a
print(x)
print(y)
print(z)
