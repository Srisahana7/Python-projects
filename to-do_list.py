# To-do list 

# Features:
# Add task
# View task
# Search task
# Delete task
# completed task
# Exit system


print("1. Add task")
print("2. View task")
print("3. Search task")
print("4. Remove task")
print("5. Update task")
print("6. Exit")

task_list = []

pending_task = []

completed_task = []

task_list.append(pending_task)
task_list.append(completed_task)

#adding task
def add_task():

    n = input("How many task you want to added = ")
    if not n.isdigit():
        print("You typed invalid input", n ,"type only numbers")
    else:
        n = int(n)
        task_mode = input("You want to add pending or completed tasks p/c : " )

        if task_mode == 'p' or task_mode == 'c':
            for i in range(n):
                task = input("task :" )
                if task_mode == 'p':
                    pending_task.append(task)
                    print("Task added successfully")
                    
                elif task_mode == 'c':
                    completed_task.append(task)
                    print("Task added successfully")

                else:
                    print("You typed invalid alphabet", task_mode, "only type c or p")
            print("All tasks: ",task_list)

# searching task           
def search_task():

    task = input("Enter the task which you want to search: ")

    if not any(char.isalnum() for char in task):
        print("You typed invslid input", task)
        
    else:
        
        if task in pending_task:
            index = pending_task.index(task)
            print(task, "is found in pending task list at the position", index+1)

        elif task in completed_task:
            index = completed_task.index(task)
            print(task, "is found in completed task list at the position", index+1)

        else:
            print("Task is not found")

#removing the task
def remove_task():
    n = input("How many task you want to delete= ")
    if not n.isdigit():
        print("You entered invalid input", n)
    else:
        n = int(n)
        for i in range(n):
            task = input("Which task you want to delete: ")
            if not any(char.isalnum() for char in task):
                print("You typed invalid input",task)
            else:
                if task in pending_task:
                    pending_task.remove(task)
                    print("Removed successfully")
                elif task in completed_task:
                    completed_task.remove(task)
                    print("Removed successfully")
                else:
                    print("Your task", task, "is not found")


#update task
def update_task():

    task = input("Enter the which you want to update: ")
    if task not in pending_task and task not in completed_task:
        print("Your task", task, "is not in the task list")

    elif task in pending_task:
        pending_task.remove(task)
        completed_task.append(task)
        print("Task marked as completed")

    else:
        print("Task is already in completed list")

# view task
def view_task():

    if not pending_task and not completed_task:
        print("There is no task in tasklist")

    else:
        for i, task in enumerate(pending_task, start=1):
            print("Pending task: ",i, ".", task)
    
        for i, task in enumerate(completed_task, start=1):
                print("Completed task:", i, ".", task)

while True:
    option = input("Enter option = ")

    if option.isdigit():
        if option == '1':
            add_task()
        elif option == '2':
            view_task()
        elif option == '3':
            search_task()
        elif option == '4':
            remove_task()
        elif option == '5':
            update_task()
        elif option == '6':
            print("Exiting....")
            break
        else:
            print("You entered invalid option")

    
