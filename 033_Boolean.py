"""
File: Boolean.py
Author: Moataz Elhawary
Date: 2024-09-10
"""

# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects ( False ) or ( True ).
# ---------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# True Values
print(bool("Moataz"))
print(bool(100))
print(bool(100.45))
print(bool(True))

print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False Values
print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))
