import random
choose = ['Rock', "Paper", "Scissors"]
computer_choice = random.choice(choose)
print(computer_choice)

print("Welcome to the Rock, Paper, Scissors game ")
choice = input("Press 'Enter' to continue or type 'Help' for the rules :   " )
help = '''
********RULES**********
1) You choose and the computer choose
2)/Rock smashes Scissors -> Rock win
3)Scissors cut paper -> Scissors win
4)Paper covers Rock -> Paper win
'''

if choice.lower()  == "help":
    print(help)
choice = input("Enter your choice (rock , paper, scissors) : ").capitalize()
if choice.capitalize() == computer_choice:
    print("It's tea!")
elif choice.capitalize() not in choose:
    print('Invalid Input , Try again!')
elif choice == "Paper" and computer_choice == 'Rock'or choice == "Rock" and computer_choice == 'Scissors' or choice == "Scissors" and computer_choice == 'Paper' :
    print(f'''
You win ,
You choice {choice} and the computer choice {computer_choice}

    {choice} always win insted of {computer_choice}
''')
else:
    print(f"You lose ,the {computer_choice} always win insted of {choice} ")




