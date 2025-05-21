"""
File: Escape_Sequences_Characters.py
Author: Moataz Elhawary
Date: 2024-09-04 
"""

# ----------------------------
# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# ----------------------------

# Back Space // in V3.10 Worked as .
print("Hello\bWorld")  # Will Remove o

# \newline => Escape New Line + \
print("Hello \
I Love \
Python")

# \\ => Escape Back Slash
print("I Love Back Slash \\")

# \' => Escape Single Quotes
print('I Love Single Quote \'Test\'')

# \" => Escape Double Quotes
print("I Love Double Quote \"Test\"")

# \n => Line Feed (New Line)
print("Hello World\nNew Line")

# Carriage Return // in V3.10 Worked As New Line
print("123456\rAbcde")

# Horizontal Tab
print("Hello\tPython")

# Character Hex Value
print("\x4D\x6F\x61\x74\x61\x7A")
