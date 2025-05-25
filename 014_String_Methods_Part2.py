"""
File: Strings_Methods_Part2.py
Author: Moataz Elhawary
Date: 2024-09-04 
"""

# ---------------------
# -- Strings Methods --
# ---------------------

# split() Splits the string at the specified separator, and returns a list

a = "I Love Python and PHP and MySQL"
print(a.split())
# print(type(a.split()))

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))  # Split Take Separator

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 2))  # Split Take Separator and Max Split

# rsplit() Splits the string at the specified separator, and returns a list
d = "I-Love-Python-and-PHP-and-MySQL"

print(d.rsplit("-", 2))  # return two splits from Right


# center() Returns a centered string
e = "Moataz"
print(e.center(10))
print(e.center(10, "*"))
print(e.center(10, "&"))


# count() Returns the number of times a specified value occurs in a string
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))
print(f.count("PHP", 0, 25))  # Only One PHP


# swapcase() Swaps cases, lower case becomes upper case and vice versa
g = "I Love Python"
h = "i love pYTHON"
print(g.swapcase())
print(h.swapcase())

# startswith() Returns true if the string starts with the specified value
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith() Returns true if the string ends with the specified value
j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))  # Love


# ---------------------
# ---- Conclusion -----
# ---------------------

# capitalize()	Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	    Returns a centered string
# count()	    Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	    Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isascii()	    Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	    Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	    Returns a left justified version of the string
# lower()	    Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()	    Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	    Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()	    Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	    Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	    Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	    Converts a string into upper case
# zfill()	    Fills the string with a specified number of 0 values at the beginning
