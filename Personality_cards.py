user_country = input("Where are you from :  ")
if user_country.capitalize() == "Yemen":

    user_age = int(input("How old are you  :  "))
    if user_age >= 18 :
        print("You can cut a card..")
    else:
        print("Wait until you growen to 18!")
else:
    print("The card just free for the Yementions!")