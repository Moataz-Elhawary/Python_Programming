"""
File: Strings_Indexing_and_Slicing.py
Author: Moataz Elhawary
Date: 2024-09-04 
"""

# ---------------------------------
# Strings Indexing & Slicing
# ---------------------------------
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets [] To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------


# Indexing (Access Single Item)

myString = "I Love Python"
print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t
print(myString[-1])  # Index -1 => n First Character From End
print(myString[-6])  # Index -6 => P 6th  Character From End


# Slicing ( Access Multible Sequence Items )
# [Start : End] End Not Encluded
# [Start : End : Steps]

print(myString[8:11])  # print yth
print(myString[3:5])  # print ov


print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here WillGo to The End  Print (e Python)

print(myString[:])  # Print Full String Full Data

print(myString[0::1])  # Print Full String Full Data With one Step
print(myString[::1])  # Print Full String Full Data With one Step

print(myString[::2])  # With Two Step
print(myString[::3])  # With Three Step
