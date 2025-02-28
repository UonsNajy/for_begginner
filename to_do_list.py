done_tasks = []
not_yet_tasks = []
tasks = input("Enter your tasks for today separated by a comma:  ").split(", ")
for task in tasks:
    if task:
        print(task)

        if_finish = input(f"Do you finish {task} alredy (y/n):   ")
        if if_finish.lower() == "y":
            print("Nice job!")
            print("-----------")
            done_tasks.append(task)
        elif if_finish.lower() == "n":
            print("Try not to put it off!")
            print('----------------------')
            not_yet_tasks.append(task)
        else:
            print("Invalid input , try later.")
choice = input("Do you want to see your today's progress? (y/n) :   ")
if choice.lower() == "y":
    print("******Done Tasks******")
    print(done_tasks)
    print("")
    print("--------------")

    print("******Ongiong Tasks******")
    print(not_yet_tasks)
    print("")
    print("--------------")
elif choice.lower() == "n":
    input("Press 'enter to exit'")
else:
    print("Invalid input, Try again.")
    
