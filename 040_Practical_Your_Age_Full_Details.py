"""
File: Practical_Your_Age_full_Details.py
Author: Moataz Elhawary
Date: 2024-09-10
"""


# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age
age = int(input("What's Your Age ?").strip())

# Get Age In All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("Your Lived For :")
print(f"{months} Month.")
print(f"{weeks:,} Week.")
print(f"{days:,} Day.")
print(f"{hours:,} Hour.")
print(f"{minutes:,} Minute.")
print(f"{seconds:,} Second.")
