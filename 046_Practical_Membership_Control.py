"""
File: Practical_Membership_Control.py
Author: Moataz Elhawary
Date: 2024-09-11
"""


# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Moataz", "Mohamed", "Enas", "Mohab", "Moamen"]

# Login
name = input("Please Type Your Name : ").strip().capitalize()

# If Name is In Admin
if name in admins:
    print(f"Hello {name} , Welcome Back .")
    option = input("Delete or Updete Your Name ?").strip().capitalize()

    # Update option
    if option == 'Updete' or option == 'U':

        NewName = input("Please Type Your New Name : ").strip().capitalize()
        admins[admins.index(name)] = NewName
        print("Name Updeted .")
        print(admins)

    # Delete option
    elif option == 'Delete' or option == 'D':

        admins.remove(name)
        print("Name Deleted .")
        print(admins)

    # Wrong option
    else:
        print("WRONG OPTION .!")

else:
    status = input("Not Admin , Add You ? y \\ N ").strip().capitalize()

    if status == 'Yes' or status == 'Y':
        yourName = input("Please Type Your Name : ").strip().capitalize()
        print("Name Added .")
        admins.append(yourName)
        print(admins)

    else:
        print("You Are Not Added . ")
