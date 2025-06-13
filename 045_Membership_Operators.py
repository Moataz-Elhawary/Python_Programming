"""
File: Membership_Operators.py
Author: Moataz Elhawary
Date: 2024-09-11
"""


# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Moataz"
print("M" in name)
print("z" in name)
print("O" in name)

print("#" * 50)

# List
Frinds = ["Ahmed", "Moataz", "Osama", "Omar"]
print("Omar" in Frinds)  # True
print("Ali" in Frinds)  # False
print("Mahmoud" not in Frinds)  # True

print("#" * 50)

# Using in and not in With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Egypt"

if myCountry in countriesOne:
    print(f"Hello, You Have A Discount Equal To ${countriesOneDiscount}")

elif myCountry in countriesTwo:
    print(f"Hello, You Have A Discount Equal To ${countriesTwoDiscount}")

else:
    print("You Have No Discount.!")
