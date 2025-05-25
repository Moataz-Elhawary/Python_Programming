"""
File: Strings_Methods_Part1.py
Author: Moataz Elhawary
Date: 2024-09-04 
"""

# ---------------------
# -- Strings Methods --
# ---------------------


# len() Function To Determine length Of String
a = "I Love Python"
print(len(a))

# ----------------------------------------------------------------------------------------#
# strip()  rstrip() lstrip()

a = "    I Love Python    "
# Return a copy of the string with leading and trailing whitespace removed
print(a.strip())
print(a.rstrip())
print(a.lstrip())


a = "#####I Love Python#####"
# If chars is given and not None, remove characters in chars instead.
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))


a = "#@#@#@I Love Python#@#@#@"
# If chars is given and not None, remove characters in chars instead.
print(a.strip("#@"))
print(a.rstrip("#@"))
print(a.lstrip("#@"))

# ----------------------------------------------------------------------------------------#

# title()
b = "I Love 2d Graphics and 3g Technology and Python"
print(b.title())


# capitalize()
b = "i Love 2d graphics and 3g technology and python"
print(b.capitalize())

# ----------------------------------------------------------------------------------------#

# zfill() Zero Fill

c, d, e, f = "1", "11", "111", "1111"
print(c)
print(d)
print(e)
print(f)
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# ----------------------------------------------------------------------------------------#

# upper()

g = "moataz"
print(g.upper())

# upper()

h = "MOATAZ"
print(h.lower())

# ----------------------------------------------------------------------------------------#
