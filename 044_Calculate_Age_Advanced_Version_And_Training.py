"""
File: Calculate_Age_Advanced_Ver_And_Training.py
Author: Moataz Elhawary
Date: 2024-09-11
"""


# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
print('#' * 80)
print(" You Can Write The First Litter Or Full Name Of The Time Unit " .center(80, '#'))
print('#' * 80)

# Collect Age Data
age = input("Please Write Your Age : ").strip()


# Collect Time Unit Data
unit = input("Please Choose Time Unit : Months, Weeks, Days : ").strip().lower()


# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365


if unit == 'months' or unit == "m":
    print("You Choosed The Unit Months. ")
    print(f"You Lived For {months:,} Month. ")

elif unit == 'weeks' or unit == 'w':
    print("You Choosed The Unit Weeks. ")
    print(f"You Lived For {weeks:,} Week. ")

elif unit == 'days' or unit == "d":
    print("You Choosed The Unit Day. ")
    print(f"You Lived For {days:,} Day. ")
