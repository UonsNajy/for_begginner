library_books = []
wish_list = []

while True:       
    own_book = input("Enter the first name of your first book in your labrary :  ")
    if own_book:
        library_books.append(own_book)
        
        own_book_2 = input("Enter the second name of your first book in your labrary or press 'enter' to scrip:  ")
        if own_book_2:
            library_books.append(own_book_2)

            print(f"Yoyr library {library_books}")
            wish_book = input("Enter thr name of the book you wish to get it in the future :  ")
            if wish_book:
                wish_list.append(wish_book)
                wish_book_1 = input("Enter the name of the other book you wish to git it in the future (or press enter to skip) :  ")
                if wish_book_1 :
                    wish_list.append(wish_book_1)
                    print(f"you wishlist {wish_list}")
                    got_it = input("Enter the name of the book from your wishlist that you've acquired (or press enter to skip ) :  ")
                    if got_it:
                        library_books.append(got_it)
                        print(f"Update library {library_books}")
                        wish_list.remove(got_it)
                        print(f"Updata wishlist {wish_list}")
                    

                        
                        donated_book = input("Enter the name of the book that you wish to donation it (or press enter to skip) : ")
                        if donated_book:
                            library_books.remove(donated_book)
                            print(f"Final book after Donations : {library_books}")  

                        else: 
                            print("The space is empty.")
                            print(f"Ok , Final book without Donata {library_books}")
                            break
                 
                    else:
            
                        print("The space is empty.")
                        print(f"Update library {library_books}")
                        print(f"Updata wishlist {wish_list}")
                        donated_book = input("Enter the name of the book that you wish to donation it (or press enter to skip) : ")
                        if donated_book:
                            library_books.remove(donated_book)
                            print(f"Final book after Donations : {library_books}")  

                        else: 
                            print("The space is empty.")
                            print(f"Ok , Final book without Donata {library_books}")
                            break

                
            else:
        
                print("The space is empty.")
        
            
        else:
        
            print(f"Yoyr library {library_books}")
            

    else:
        print("The space is empty.")
          

