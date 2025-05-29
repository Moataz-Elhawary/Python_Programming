"""
File: Dictionary.py
Author: Moataz Elhawary
Date: 2024-09-09
"""

# ----------------------------
# -- Dictionary --
# ----------------------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------


# Dictionary

user = {
    "Name": "Moataz",
    "Age": 27,
    "Country": "Egypt",
    "Skills": ["Python", "C", "C++"],
    "Rating": 10.5
}

print(user)

print(user['Country'])
print(user.get("Country"))

print(user.keys())
print(user.values())

print("=" * 50)


# Two-Dimensional Dictionary

languages = {
    "One": {
        "name": "Html",
        "progress": "80%"
    },
    "Two": {
        "name": "css",
        "progress": "70%"
    },
    "Three": {
        "name": "JS",
        "progress": "90%"
    }
}

print(languages)
print(languages["One"])
print(languages['Three']['name'])

print("=" * 50)

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

print("=" * 50)


# Create Dictionary from Variables

freamworkOne = {
    "name": "vuejs",
    "progress": "80%"
}
freamworkTwo = {
    "name": "ReactJs",
    "progress": "70%"
}
freamworkThree = {
    "name": "Angular",
    "progress": "90%"
}

allfreamwork = {
    "one": freamworkOne,
    "two": freamworkTwo,
    "three": freamworkThree
}

print(allfreamwork)
