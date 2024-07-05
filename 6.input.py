name = input("what is your name?: ")
age = int(input("how old are you?: "))
height = float(input("how tall are you (feet)?: "))

age += 1
height = height*30.48


print("hello " + name)
print("your age next year: " + str(age))
print("your height (cm): " + str(height))


