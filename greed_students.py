import time
not_end = True
while not_end:
        
    greed = float(input("Enter your greed :%"))

    if greed >= 90 and greed <= 101:
        print("Exllant!")

        choice = input("Do you want to continue (y/n) : ")
        if choice == "y":
            print('')
            
            time.sleep(5)
        elif choice == 'n' :
            break
        else:
            print("Invalid choice , try again after 5 minutes")

    elif greed >=75 and greed < 90:
        print("Good! ")
        choice = input("Do you want to continue (y/n) : ")
        if choice == "y":
            print('')
            
            time.sleep(5)
        elif choice == 'n' :
            break
        else:
            print("Invalid choice , try again after 5 minutes")   
    elif greed >=50 and greed < 90:
        print("Not bad! ")
        choice = input("Do you want to continue (y/n) : ")
        if choice == "y":
            print('')
            
            time.sleep(5)
        elif choice == 'n' :
            break
        else:
            print("Invalid choice , try again after 5 minutes")    
            

    elif greed <= 49:
        print("Week! ")
        choice = input("Do you want to continue (y/n) : ")
        if choice == "y":
            print('')
            
            time.sleep(5)
        elif choice == 'n' :
            break
        else:
            print("Invalid choice , try again after 5 minutes")
          
    else:
        print("Invalid input,try again after 5 minutes......")
        r
