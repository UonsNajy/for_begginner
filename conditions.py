area = input("Chose an area : (Sana'a , Aden or Tais) :  ")

if area.lower() == "sana'a" or area.upper() == 'ADEN' or area.capitalize() == "Tais" :
    print(f"{area} is nice! and it's in or list" )

else:
    print("Invalid input , Try agian.")