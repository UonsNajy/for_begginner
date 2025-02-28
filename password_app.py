guess_password = input('Enter the password : ')

if guess_password.lower() == "abc":
    print("Welcome back , the password is true.")

else:
    print("invalid password!")



words = ['yes','no','maybe']
choice = input('Enter (Yes/No/maybe) :  ')
if choice.lower() in words :
    print(f"You typed {choice}")
else:
    print("Invalid input!")

guess_num = int(input("Enter a number : "))
if guess_num == 7:
    print("Correct")
else("Wrong!")