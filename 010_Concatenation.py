"""
File: Concatenation.py
Author: Moataz Elhawary
Date: 2024-09-04 
"""

# -------------------
# -- Concatenation --
# -------------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)

# Another Mwthod
full = msg + " " + lang
print(full)


a = "First \
Second \
Third"

b = "A \
B \
C"

print(a + " " + b)


# Not Valid (ERROR) because Concatenation Can Only Concatenate (str to str) NOT int
print("Hello" + 1)
