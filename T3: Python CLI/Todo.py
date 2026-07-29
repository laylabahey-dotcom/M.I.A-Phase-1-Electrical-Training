#this library + commands to save the textfile to wherever the script is
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "Todolist.txt")

#array/list that stores tasks
tasks = ["Fill up on gas", "Clean the interior", "Check on tires", "Attend Photoshoot"]

#create file and save tasks if the array/list has any to record to file
#tasks are written only if the file is new, or it doesnt exist, or empty
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("     LIGHTNING MCQUEEN'S TO-DO LIST      \n")
        # seeing as its 0 index, the numbering for order will be incremented by one
        # the line after each task recorded in file will have the pending status unless McQueen chooses
        # to change status to done
        for i in range(len(tasks)):
            f.write(f"{i+1}) ")
            f.write(tasks[i] + "\n")
            f.write("Pending \n")

#because there is no need to inspect lines or edit them, using f.read() is enough for just viewing the list as a block.
def view_list():
    with open(filename, "r") as f:
        content = f.read()
        print(content)

#to add a task, the order number must be known. That is calculated first, casting needed so that it isn't a float. 
# f.readlines() is important because it stores each line as an element in a list, making it easiest way to find which task_number we are on,
#then the task passed onto the function is appended onto the end of it
def add_task(task):
    with open(filename, "r") as f:
        lines = f.readlines()
    task_number = int(len(lines) / 2 + 1)

    with open(filename, "a") as f:
        f.write(f"{task_number}) ") 
        f.write(task + "\n")
        f.write("Pending \n")
    print("Here's your brand new long list now!\n")
    view_list()

# same as past functions, f.readlines() is necessary to determine which task the task_number is pointing at
# the status index is calculated to pin done which Pending should be turned into a done
def mark_as_done(task_number):
    with open(filename, "r") as f:
        lines = f.readlines()
        status = (task_number - 1)* 2 + 2

        if status >= 0 and status< len(lines) :
            #overwrite pending into a done
            lines[status] = "Done \n"
            #rewrite the whole lines back into the folder
            with open(filename, "w") as f:
                f.writelines(lines)
            print("Done and done, boss!")
            view_list()
        else:
            print("No such task, Kachow!")

#following same concept as past 2 functions, but using del functions the unwanted tasks and their status is removed 
# then the file is rewritten
def remove_task(task_number):
    with open(filename, "r") as f:
            lines = f.readlines()
            text_index = (task_number - 1)* 2 + 1
            status = text_index + 1
    
            if status >= 0 and status < len(lines):
                task_index = status - 1
                del lines[task_index:status +1]
                #numbering new to avoid confusion
                n = 1
                for i in range(1, len(lines), 2):
                    # parition function that disregards ) and the space after it, keeping only task description
                    # then the numbers are rewritten and the n is incremented
                    _, _, task_text = lines[i].partition(") ")  
                    lines[i] = f"{n}) {task_text}"
                    n += 1
                    

                with open(filename, "w") as f:
                    f.writelines(lines)
                print("Lighter workload achieved, boss!")
                view_list()
            else:
                print("Task not found! Look again!")


#this condition equals C--> while(1) and then being exited through a return -1 (here as break). 
#Program is on loop until user decides to exit
while True:
    # The startup menu from which the user chooses a certain command 
    print("     LIGHTNING MCQUEEN'S TO-DO LIST      ")
    print("1. Add a task \n2. View my to-do list \n3. Mark a task as done \n4. Remove a task \n5. Quit")
    choice = int(input("What's the move, champ?! (1/2/3/4/5): "))

    #command number decides which functions are called
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
        break
    #default case for if the input is wrong
    else:
        print("No can do! Try again!")

            

                
       
