"""
File: Strings_Methods_Part3.py
Author: Moataz Elhawary
Date: 2024-09-04 
"""

# ---------------------
# -- Strings Methods --
# ---------------------


# index(SubString, Start, End)
a = "I Love Python"
print(a.index("P"))  # index nuber 7
print(a.index("P", 0, 10))  # index nuber 7
# print(a.index("P", 0, 5))  # Trough ERROR

# find(SubString, Start, End)
b = "I Love Python"
print(b.find("P"))  # index nuber 7
print(b.find("P", 0, 10))  # index nuber 7
print(b.find("P", 0, 5))  # -1


# rjust(width, fill cahr)
c = "Moataz"
print(c.rjust(10))
print(c.rjust(10, "#"))

# ljust(width, fill cahr)
d = "Moataz"
print(d.ljust(10))
print(d.ljust(10, "#"))


# splitlines()

e = """First Line 
Second Line 
Third Line """
print(e.splitlines())
print(type(e.splitlines()))

f = "Firdst Line\nSecond Line\nThird Line"
print(f.splitlines())


# expandtabs()
g = "Hello\tWorld\tI\tLove\tPython"
print(g)
print(g.expandtabs(2))
print(g.expandtabs(20))

one = "I Love Python And 3G"
Two = "I Love Python And 3g"
print(one . istitle())
print(Two . istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "Moataz_Elhawary"
eight = "MoatazElhawary100"
nine = "Moataz--Elhawary100"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaaaaaBbbbbbb"
y = "AaaaaaaaaBbbbbbb11111"
print(x.isalpha())  # alpha (A-Z)
print(y.isalpha())  # because included number

u = "AaaaaaaaaBbbbbbb"
z = "AaaaaaaaaBbbbbbb11111"
print(u.isalnum())
print(z.isalnum())
