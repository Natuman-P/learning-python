temp = int(input("What is the temperature outside:? "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today.")
    print("touch grass.")
elif temp < 0 or temp > 30:
    print("the temperature is bad today.")
    print("stay inside.")

# 'not' operator example:
# if not(temp >= 0 and temp <= 30):
#     print("the temperature is bad today.")
#     print("stay inside.")
# elif not(temp < 0 or temp > 30):
#     print("the temperature is good today.")
#     print("touch grass.")




