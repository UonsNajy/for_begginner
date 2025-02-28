friends_list= input("Enter your freinds names(The first name and the last name) saparated by a comma :  ").split(",")

for name in friends_list:
    names= name.split()
    print(names)

    f_name = names[0][0]
    s_name = names[1][0]

    

    all_letters = f_name +'.' +s_name+'.'


print("Abbreviated Names : ")
print(all_letters)
for i in all_letters:
    print(i)