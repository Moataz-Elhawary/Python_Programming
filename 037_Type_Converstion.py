"""
File: Type_Conversation.py
Author: Moataz Elhawary
Date: 2024-09-10
"""


# ---------------------
# -- Type Conversion --
# ---------------------

# str()
a = 20
print(type(a))
print(type(str(a)))

print("=" * 50)

# tuple()
# c = "Moataz"  # string
# d = [1, 2, 3, 4, 5]  # list
# e = {"A", "B", "C"}  # set
# f = {"A": 1, "B": 2}  # dict

# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))
print("=" * 50)


# list()
# c = "Moataz"  # string
# d = (1, 2, 3, 4, 5)  # tuple
# e = {"A", "B", "C"}  # set
# f = {"A": 1, "B": 2}  # dict

# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))
print("=" * 50)


# set()
# c = "Moataz"  # string
# d = (1, 2, 3, 4, 5)  # tuple
# e = ["A", "B", "C"]  # list
# f = {"A": 1, "B": 2}  # dict

# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))
# print("=" * 50)


# dict

d = (("A", 1), ("B", 2), ("C", 3))  # Nested Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # Nested list


print(dict(d))
print(dict(e))

print("=" * 50)
