"""
File: Strings_Formatting.py
Author: Moataz Elhawary
Date: 2024-09-05 
"""

# -----------------------------------
# --- Strings Formatting Old Ways ---
# -----------------------------------

# name = "Moataz"
# age = 27
# rank = 10

# print("My Name Is : " + name)

# # print("My Name Is : " + name "end My Age Is : " + age) # Type Error because can only concatenate str to str should be use formatting by place holder
# print("My Name is : %s" % name)
# print("My Name is : %s and My age is : %d" % (name, age))
# print("My Name is : %s and My age is : %d and My Rank is : %f" % (name, age, rank))

# # %s => String
# # %d => Number
# # %f => Float

# n = " Moataz"
# l = "Python"
# y = 1

# print("My Name is %s I'm %s Developer With %d Years Exp " % (n, l, y))


# # Control Floating Point Number

# myNumber = 10
# print("My Number is : %d " % myNumber)
# print("My Number is : %f " % myNumber)
# print("My Number is : %.2f " % myNumber)

# # Truncate String

# myLongString = "Hello People I Love You All"
# print("Message is : %s" % myLongString)
# print("Message is : %.5s" % myLongString)


# -----------------------------------
# --- Strings Formatting New Ways ---
# -----------------------------------

name = "Moataz"
age = 27
rank = 10

print("My Name is : {}".format("Moataz"))
print("My Name is : {}".format(name))
print("My Name is : {} and My age is : {}".format(name, age))
print("My Name is : {:s} age : {:d} & Rank is : {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float


# Control Floating Point Number

myNumber = 10
print("My Number is : {:d} ".format(myNumber))
print("My Number is : {:f} ".format(myNumber))
print("My Number is : {:.2f} ".format(myNumber))


# Truncate String
myLongString = "Hello People I Love You All"
print("Message is : {}".format(myLongString))
print("Message is : {:.5s}".format(myLongString))
print("Message is : {:.13s}".format(myLongString))


# Format Money

MyMoney = 500162354740
print("My Money in Bank is : {:d}".format(MyMoney))
print("My Money in Bank is : {:_d}".format(MyMoney))
print("My Money in Bank is : {:,d}".format(MyMoney))


# ReArrange Item


a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {1} {0}".format(a, b, c))  # Hello Three Two One

x, y, z = 10, 20, 30

print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))


# Format in version 3.6 or above

myName = "Moataz"
myAge = 27

print("My Name is : {myName} and my Age is : {myAge}")
print(f"My Name is : {myName} and my Age is : {myAge}")
