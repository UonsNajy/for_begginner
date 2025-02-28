print("Welcom in the rabbit place")
print('')

field  = [['graps','graps',"graps"], ['graps','graps',"graps"], ['graps','graps',"graps"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}")

print("where should the rabbit go? 'rabbit'")

position = input("Please, choose a row and a column :  ")

row = int(position[0])
column = int(position[1])

field[row-1][column-1] = "rabbit"

print("Succesful...")


print(f"{field[0]}\n{field[1]}\n{field[2]}")

