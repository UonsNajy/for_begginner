import random

print("*** Welcome to 'whose wallet' ***")
print("")
print("You will give me a list of names, and I will pick a person to pay ")
names = input("If you are already enter the names separated by a comma :  ").split(", ")
will_pay =random.choice(names)
print(f"Please ,asked '{will_pay}' to take his wallet out. Dinner is on him!")