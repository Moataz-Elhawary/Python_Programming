"""
File: User_Input.py
Author: Moataz Elhawary
Date: 2024-09-10
"""


# ----------------
# -- User Input --
# ----------------

First_Name = input("What's Your First Name? : ")
Middle_Name = input("What's Your Middle Name? : ")
Last_Name = input("What's Your Last Name? : ")

First_Name = First_Name.strip().capitalize()
Middle_Name = Middle_Name.strip().capitalize()
Last_Name = Last_Name.strip().capitalize()

print(f"Hello {First_Name} {Middle_Name:.1s} {Last_Name} , Happy To See You .")
