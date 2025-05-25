"""
File: Strings_Methods_Part4.py
Author: Moataz Elhawary
Date: 2024-09-05 
"""

# ---------------------
# -- Strings Methods --
# ---------------------

# replace (Old Value, New Value, Count) Returns a string where a specified value is replaced with a specified value

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))


# join() Joins the elements of an iterable to the end of the string we should to use separator first

myName = ["Moataz", "Mohamed", "Elhawary"]
print("-".join(myName))
print(" ".join(myName))
print(".".join(myName))
print(type(".".join(myName)))  # return String Type
