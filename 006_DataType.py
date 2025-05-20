"""
File: DataType.py
Author: Moataz Elhawary
Date: 2024-09-03 
"""
# ------------------------------
# Type()
# All Data in Python is Object
# ------------------------------


print(type(10))    # <class 'int'> =>   Integer
print(type(100))   # <class 'int'> =>   Integer
print(type(1000))  # <class 'int'> =>   Integer
print(type(-10))   # <class 'int'> =>   Integer

print(type(100.90))  # <class 'float'> => Floating Point Number
print(type(1.98))    # <class 'float'> => Floating Point Number
print(type(-10.60))  # <class 'float'> => Floating Point Number

print(type("Hello Python"))     # <class 'str'> => String

print(type([1, 2, 3, 4, 5]))    # <class 'list'> => List

print(type((1, 2, 3, 4, 5)))    # <class 'tuple'> => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # <class 'dict'> => Dictionary

print(type(2 == 2))  # <class 'bool'> => Boolean (True or False)
