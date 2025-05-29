"""
File: Set.py
Author: Moataz Elhawary
Date: 2024-09-09 
"""

# --------------------------------
# -- Set --
# --------------------------------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# --------------------------------

# Not Ordered And Not Indexed

mySetOne = {"Moataz", "Mohamed", 100}
print(f"My Set One IS : {mySetOne}")
# print(mySetOne[0]) # Not Valid


# mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])  # Not Valid


# Has Only Immutable Data Types

# mySetThree = {"Moataz", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Moataz", 100, 100.5, True, (1, 2, 3)}
print(f"My Set Three Is : {mySetThree}")


# Items Is Unique

mySetFour = {1, 2, "Moataz", "One", "Moataz", 1}
print(f"my Set Four Is : {mySetFour}")
