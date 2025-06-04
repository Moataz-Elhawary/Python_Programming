"""
File: Control_Flow_If_elIf_else.py
Author: Moataz Elhawary
Date: 2024-09-11
"""


# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Moataz"
uCountry = "KSA"
cName = "python Course"
cPrise = 100


if uCountry == "Egypt":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Prise Is : ${cPrise - 80}")

elif uCountry == "KSA":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Prise Is : ${cPrise - 60}")

elif uCountry == "Kuwait":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Prise Is : ${cPrise - 50}")

else:
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Prise Is : ${cPrise - 30}")
