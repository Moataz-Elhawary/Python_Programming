"""
File: Control_Flow_Ternary_Conditional_Operators.py
Author: Moataz Elhawary
Date: 2024-09-11
"""


# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "K "

if country == "Egypt" : print(f"The Weather in {country} is 15 ")
elif country == "KSA" : print(f"The Weather in {country} is 30 ")
else : print("Country is Not in The List")

# Short if 

movieRate = 18
age = 18

if age < movieRate : print ("Movie Is Not Good 4U") # Condition if True 
else : print ("Movie Is Good 4U And Happy Watching") # Condition if False 


# Condition If True | If Condition | Else | Condition If False
print("Movie Is Not Good 4U" if age < movieRate else "Movie Is Good 4U And Happy Watching" )
