def intru():

    print("*********Run the app**********")
    print("         Main Menu          ")
    print ("")
intru()

class Player():
    def __init__(self, name,symbol):
        self.name = name
        self.symbol = symbol

    def create_player(self):

        self.name= input('Enter your first name :  ').lower()
        while True:
            
            symbol = input('Enter Symbol (single Letter):  ')
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol
                break
            else:
                print("Invalid input! please try again")

playerr= Player()  

playerr.create_player()

























# def run_game():
#     game_on = True
#     while game_on:

#         choice = input("Start the game or Git out the game (s/g) :  ").lower()

#         if choice == 's':
            
#         elif choice == 'g':
#             print('Thanks for visited us!')
#             break

#         else:
#             print('Invalid input!')

# run_game()