"""
File: Loop_While_Training_bookmark_Manager.py
Author: Moataz Elhawary
Date: 2024-09-12
"""

# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later
myFavoriteWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0:
    # Input The New Website
    web = input("Website Name Without https:// ")

    # Add The New Website To The List
    myFavoriteWebs.append(f"https://{web.strip().lower()}")

    # Decrease One Number From Allowed Websites
    maximumWebs -= 1

    # Print The Add Massage
    print(f"Website Added , {maximumWebs} Places Left .")

    # Print The List
    print(myFavoriteWebs)

else:
    print("Bookmark Is Full, You Can't Add More ..! ")


# Check If List Is Not Empty
if len(myFavoriteWebs) > 0:

    # Sort The List
    myFavoriteWebs.sort()

    index = 0
    print("Printing The List Of Websites in Your Bookmark ")

    while index < len(myFavoriteWebs):
        print(myFavoriteWebs[index])
        index += 1
