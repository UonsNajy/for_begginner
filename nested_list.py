# basket = [['apple','banana'],['milk','water']]
# basket.append(["cake",'Candy'])
# basket.insert(2,"caffe")
# print(basket)


# books = ['book1','book3','book5']
# books.insert(1,'book2')
# books.insert(3,'book4')
# books.insert(5,'book6')
# books.insert(-1,'book6')
# print(books)



basket = [['apple','banana'],['milk','water']]
print(basket)
basket[1].remove("water")
basket[0].append("kiwais")
basket[0].insert(0, 'oranges')
basket[1].insert(0, 'coffee')
basket[1].insert(2, 'tea')
basket.append([1,2,3])

input("Press enter to change the content...........")

print("")
print("Here is the upsated basket : ")
print(basket)
