
filename = r"C:\Users\layla\OneDrive\Desktop\M.I.A Training\Session 3 - Python and Git\Todolist.txt"
tasks = []

with open(filename, "a") as f:
    for i in range(len(tasks)):
        f.write("     LIGHTNING MCQUEEN'S TO-DO LIST      ")
        f.write(f"{i+1}) ")
        f.write(tasks[i] + "\n")
        f.write("Unfinished \n")

def view_list():
    with open(filename, "r") as f:
        content = f.read()
        print(content)

def add_task(task):
    with open(filename, "r") as f:
        lines = f.readlines()
    task_number = int(len(lines) / 2 + 1)

    with open(filename, "a") as f:
        f.write(f"{task_number}) ") 
        f.write(task + "\n")
        f.write("Unfinished \n")
    print("Here's your brand new long list now!\n")
    view_list()

def mark_as_done(task_number):
    with open(filename, "r") as f:
        lines = f.readlines()
        stat_idx = (task_number - 1)* 2 + 1

        if stat_idx >= 0 and stat_idx< len(lines) :
            lines[stat_idx] = "Done \n"
            with open(filename, "w") as f:
                f.writelines(lines)
            print("Done and done, boss!")
            view_list()
        else:
            print("No such task, Kachow!")

def remove_task(task_number):
    with open(filename, "r") as f:
            lines = f.readlines()
            stat_idx = (task_number - 1)* 2 + 1
    
            if stat_idx >= 0 and stat_idx< len(lines):
                text_idx = stat_idx - 1
                del lines[text_idx:stat_idx+1]
                with open(filename, "w") as f:
                    f.writelines(lines)
                print("Lighter workload achieved, boss!")
                view_list()
            else:
                print("Task not found! Look again!")



while True:
    print("     LIGHTNING MCQUEEN'S TO-DO LIST      ")
    print("1. Add a task \n2. View my to-do list \n3. Mark a task as done \n4. Remove a task \n5. Quit")
    choice = int(input("What's the move, champ?! (1/2/3/4/5): "))

    if choice == 1:
        task = input("Alright, boss! Another task! Shoot: ")
        add_task(task)
    elif choice ==2:
        print("Want to check your progress? Sure thing!\n")
        view_list()
    elif choice == 3:
        task_number = int(input("Which task do you want to mark as marked as done?"))
        mark_as_done(task_number)
    elif choice == 4:
        print("Removing a task! Lighter workload, yay!\n")
        task_number = int(input("Which task do you want to remove?"))
        remove_task(task_number)
    elif choice == 5:
        print("Leaving so soon?! Well, bye bye!\n")
        f.close("Todolist.txt")
        break
    else:
        print("No can do! Try again!")

            

                
       