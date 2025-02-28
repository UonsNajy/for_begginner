user_name = input("Type your name : ")
user_age = int(input("Type your age : "))
user_license = input("Do you have a license (y/n) : ")
print("")
if user_age >= 18 and user_license.lower() == "y":
    print("Congratulations!You can drive.")
elif user_age <= 18 and user_license.upper() == "N":
    print("Sorry, You can't drive!")