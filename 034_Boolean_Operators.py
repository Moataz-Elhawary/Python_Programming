"""
File: Boolean_Operators.py
Author: Moataz Elhawary
Date: 2024-09-10
"""


# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 27
country = "Egypt"
rank = 10

print(age > 16)
print(country == "Egypt")
print("=" * 50)

# and
print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False
print("=" * 50)

# or
print(age > 16 or country == "Egypt" or rank > 20)  # True
print(age > 16 or country == "KSA" or rank > 0)  # True
print("=" * 50)

# not
print(age > 16)  # True
print(not age > 16)  # Not True = False
