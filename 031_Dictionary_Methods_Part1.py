"""
File: Dictionary_Methods_Part1.py
Author: Moataz Elhawary
Date: 2024-09-09
"""


# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear

user = {
    "name": "Moataz"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update

member = {
    "name": "Moataz"
}
print(member)
member["age"] = 27
print(member)

member.update({"country": "Egypt"})
print(member)

print("=" * 50)


# copy

main = {
    "name": "Moataz"
}

b = main.copy()  # Shallow Copy
print(b)

main.update({"Skill": "Fighting"})
print(main)
print(b)

print("=" * 50)

# keys () + value()

print(main.keys())
print(main.values())
