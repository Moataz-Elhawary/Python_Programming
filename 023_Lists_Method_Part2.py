"""
File: Lists_Methods_Part2.py
Author: Moataz Elhawary
Date: 2024-09-08 
"""

# -------------------
# -- Lists Methods --
# -------------------

# clear

a = [1, 2, 3, 4]
a.clear()
print(a)


# copy
b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)
print(c)


# count

d = [1, 2, 3, 5, 7,  1, 3, 1, 2, 1]
print(d.count(1))


# index

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))


# insert

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)


# pop

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))
