import random
computer_pin_code = random.randint(1,10000)

game_on = True
while game_on:
    try:

        user_pin_code = input("Enter a 4_digit PIN code :  ")
                   
          
        if len(user_pin_code) != 4:
            print('Please, Type 4_digit :')
        elif len(user_pin_code) == 4 :
            user_pin = int(user_pin_code)
        
            if user_pin == computer_pin_code:
                print(f'Congratulations, the computer generated this PIN {computer_pin_code}')
                break
            elif user_pin != computer_pin_code:
                print("Failure! PIN code did not match")
                print(f"The computer generated this PIN {computer_pin_code}")
                break
            else:
                print("Invalid input,Try again.")    
        else:
            print("Invalid input,Try again.")
    except ValueError:
        print("This is lettets I need number digits")