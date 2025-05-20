"""
File: Variables_Part1.py
Author: Moataz Elhawary
Date: 2024-09-04 
"""

# ---------------------------------------------------------------
# -- Variables --
# ---------------
# Syntax => [Variable Name] [Assignment Operator (=)] [Value]
#
# Name Convention and Rules
# [1] Can Start (a-z A-Z) or Underscore ( _ ) not Spacing
# [2] You Cannot Start With Numbers or Special Characters ( - @ $ % )
# [3] Can Include Numbers and Underscores in Var
# [4] Cannot Include Special Characters
# [5] Case Sensitive Such as [ Name is Not Like name ]
# ---------------------------------------------------------------


# [1]
_myVariable = "My Value"
print(_myVariable)


# [2]
@myVariable = "My Value"
print(@myVariable)
100myVariable = "My Value"
print(100myVariable)

# [3]
my_Variable = "My Value"
print(my_Variable)
my100Variable = "My Value"
print(my100Variable)

# [4]
my@Variable = "My Value"
print(my@Variable)

# [5]
name = "My Value"
print(Name)


# Best practise
name = "Moataz Elhawary"  # Single Word => Normal
myName = "Moataz Elhawary"  # Tow Words => Camel Case
my_name = "Moataz Elhawary"  # Tow Words => Snake Case
# Three Words Each word starts with a capital letter => Pascal Case
MyFirstName = "Moataz"
