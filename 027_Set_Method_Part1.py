"""
File: Set_Method_Part1.py
Author: Moataz Elhawary
Date: 2024-09-09 
"""

# -----------------
# -- Set Methods --
# -----------------


# clear()

a = {1, 2, 3, 4}
a.clear()
print(a)


# Uniou

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"4", "5"}

print(b | c)
print(b.union(c, x))


# add()

d = {"1", "2", "3", "4"}
d.add(5)
d.add(6)
print(d)


# copy

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)


# remove

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)


# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)


# pop()

i = {"A", True, 1, 2, 3, 4, 5, 6}
print(i.pop())  # pop random element


# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(["Html", "CSS"])
j.update(k)
print(j)
