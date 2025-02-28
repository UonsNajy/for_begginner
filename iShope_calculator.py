print("***** Welcome in iShope calculator *****")
print("")
count_items = int(input("How many items are there in your besket today?  "))

print("")
print("Let's get tp counting them.............")
all_items = []
all_price = []
for item in range(1,count_items+1):
    name_item = input(f"Please, tell me the name of the item number {item} :  ")
    all_items.append(name_item)
    
    price_item = float(input(f"What is the price of {name_item} :$  "))
    all_price.append(price_item)
choice = input("Do you like to see your entire basket (y/n) :  ").lower()
if choice == "y":
    print(all_items)
    choice = input("Do you like to see how much it'll cost? (y/n) :  ").lower()   
    if choice == "y":
        print("Buying all these items will cost : ")
        print(f"${sum(all_price)}")
    elif choice == "n":
        print("Thanks, for using the app...")
    else:
        print("Invalid input!") 
elif choice == "n":
        print("Thanks, for using the app...")
else:
        print("Invalid input!") 


