import random

guess_random = random.random()
if guess_random  > 0.5 :
    com_guess ="tails"
else:
    com_guess = "heads"
    
guess_randint = random.randint(1,2)
if guess_randint  == 1 :
     com_gues ="Tails"
else:
     com_gues = "Heads"


print("*********Welcome ro the Coin Guessing Game*********")
print("")
print("""
Chose a method to toss the coin:
      1- Using random.random
      2- Using random.randint
      """)
choice = input("Enter your chose (1/2) :  ")

if choice == "1" :
    chose = input("Enter you Guess (Heads ot Tails):  ")
    if chose.lower() == com_guess:
        
        print("")
        print("Congratulations, You win!")
        print(f"The computer coin toss result was {com_guess}")

        
    elif chose.lower() != com_guess:
         print(f"Sorry You lose! The computer guess was {com_guess} ")
    elif chose.lower() != 'tails' or chose.lower() != 'heads':
        print("Invalid input ,Try again.")

elif choice == '2':
    chose = input("Enter you Guess (Heads ot Tails):  ")
    if chose.lower() == com_gues:
        
        print("")
        print("Congratulations, You win!")
        print(f"The computer coin toss result was {com_gues}")

    

        
    elif chose.lower() != com_gues:
         print(f"Sorry You lose! The computer guess was {com_gues} ")
            
else:
    print("Invalid input ,Try again.")



