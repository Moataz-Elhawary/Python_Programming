"""
File: Control_Flow_Nested_if_And_Training.py
Author: Moataz Elhawary
Date: 2024-09-11
"""


# ---------------
# -- Nested If --
# ---------------


uName = "Moataz"
isStudent = "Yes"
uCountry = "Egypt"
cName = "python Course"
cPrise = 100


if uCountry == ("Egypt" or "KSA" or "Qatar"):

    if isStudent == "Yes":

        print(f"Hello {uName} Because You Are From {uCountry} And Student ")
        print(f"The Course \"{cName}\" Prise Is : ${cPrise - 90}")

    else:

        print(f"Hello {uName} Because You Are From {uCountry}")
        print(f"The Course \"{cName}\" Prise Is : ${cPrise - 80}")


elif uCountry == ("Kuwait" or "Bahrain"):

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Prise Is : ${cPrise - 50}")

else:

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Prise Is : ${cPrise - 30}")
