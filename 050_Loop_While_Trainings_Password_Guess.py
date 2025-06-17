"""
File: Loop_While_Trainings_Password_Guess.py
Author: Moataz Elhawary
Date: 2024-09-12
"""


# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------


tries = 4

correctPass = "Moataz@1234"

inputPass = input("Write Your Password : ")

while inputPass != correctPass:
    tries -= 1
    print(f"Wrong Password .!, {'Last' if tries == 0 else tries} Chance Left ")
    inputPass = input("Write Your Password : ")

    if tries == 0:
        print("All Tries Is Finished ")
        break

else:
    print("Correct Password .. ")
