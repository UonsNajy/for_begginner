all_names = []
names = input("Type the first and the last name of your friends saparated by a comma :  ").split(",")
for name in names:
    name_part= name.split()
    print(name_part)
    first_name = name_part[0]
    second_name = name_part[1]

    first_charctor =first_name[0]
    second_charctor =second_name[0]

    all_charcters = first_charctor +"."+second_charctor+ "."

    all_names.append(all_charcters)
print("")
for i in all_names:
    print(i)




















sentence = input('Type a sentence :   ').split()
reversed_word = sentence[::-1]
reversed_sentence = " ".join(reversed_word)

print(f'Reversed Sentence  :  {reversed_sentence}')