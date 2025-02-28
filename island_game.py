print( "********* Welcome to my island!*********")
print("""
There are tow doors in front of you . red door and blue door :       
      """)
game_on = True
while game_on:
    choice = input("which door do you want to open,please, foucse (R/B) Ana if you want to exit of the game type(e) :  ")
    if choice.lower() == "b":
        print("Opps! You choice the crocodile door .")
        print("Game Over!")
    elif choice.lower() == "r":
        print("Great! Now you opened a room")
        another_chose = input("""You found three boxes : (white/black/green) 
                              which door do you want to open (W/B/G) Ana if you want to exit of the game type(e) : 
                              """)
        if another_chose.lower() == "w":
            print("Opps ! you opened a box filled with snakes.")

        elif another_chose.lower()  == "b":
            print("Opps! You opened a box filled with spiders.")
        elif another_chose.lower() == 'g':
            print("Congratulations! You found the treasure!")
            break
        elif another_chose.lower() == 'e':
            print('Exiting........')
            break

        else:
            print("Invalid choice, try again! ")
    elif choice.lower() == 'e':
            print('Exiting........')
            break
    else:
        print("INvalid input !")
