name = "" # |used if variation == a or c|

# name = None |used if variation == b|

while len(name) == 0:
    name = input("Enter your name: ") # |variation == a|

# while not name:
#     name = input("Enter your name: ") |variation == b|

# while name == "":
#     name = input("Enter your name: ") |variation == c|

print("Hello " + name + ".")