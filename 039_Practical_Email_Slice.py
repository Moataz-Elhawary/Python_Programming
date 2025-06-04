"""
File: Practical_Email_Slice.py
Author: Moataz Elhawary
Date: 2024-09-10
"""


# ---------------------------
# -- Practical Slice Email --
# ---------------------------

# email = "moataz.elhawary311@gmail.com"

# print(email.index("@"))

# print(email[:email.index("@")])


theName = input("What's Your Name ?").strip().capitalize()
theEmail = input("What's Your Email ?").strip()

theUser = theEmail[:theEmail.index("@")]
theDomain = theEmail[theEmail.index("@")+1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your User Name Is : {theUser} \nYour Domain Is : {theDomain}")
