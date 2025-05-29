"""
File: Dictionary_Method_Part2.py
Author: Moataz Elhawary
Date: 2024-09-10
"""



# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
    "name": "Moataz"
}
print(user)
print(user.setdefault("Age", 27))
print(user)

print("=" * 50)


# popitem()
member = {
    "name": "Moataz",
    "Skill": "Python"
}
print(member)
member.update({"Age": 27})
print(member.popitem())


print("=" * 50)


# items()

view = {
    "name": "Moataz",
    "Age": 27
}
allItems = view.items()
print(view)
view["skill"] = "Python"

print(allItems)


print("=" * 50)


# fromkeys()

a = ('myKeyOne', 'myKeyTwo', 'myKeyThree')
b = "X"

print(dict.fromkeys(a, b))
