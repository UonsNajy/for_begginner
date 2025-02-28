print("*** Welcome to the multiplication table ***")
num_multip = int(input("Enter a number :  "))
print("\n Multiplication table for {num_multip}")
for number in range(1,13):
    summ = number * num_multip

    print(f"{number} * {num_multip} = {summ}")