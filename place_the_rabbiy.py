print("*** Welcome in the Rabbit Place ***")
print("")

field = [['graps','graps','graps'] ,['graps','graps','graps'] ,['graps','graps','graps'] ]
print(f'{field[0]}\n{field[1]}\n{field[2]}')
print("")
print('Where will the rabbit go ? ')
choice = input('Please, choose a row and a column :  ')

row = int(choice[0])
column = int(choice[1])


field[row-1][column-1] = 'rabbit'

print('Successful....')

print(f'{field[0]}\n{field[1]}\n{field[2]}')