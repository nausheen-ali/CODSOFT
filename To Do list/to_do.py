todo_list=[]

def show_menu():
    print("=== TO-DO LIST===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No Tasks yet!")
    else:
        print("\nTasks:")
        for i, task in enumerate(todo_list, start=1):
            status="✓"if task["done"] else "✗"
            print(f"{i}.[{status}]{task['task']}")

def add_task():
    n_tasks = int(input("How may task you want to add: "))
    for i in range(n_tasks):
        task_name = input("Enter the task:")
        todo_list.append({"task": task_name, "done": False})
        print("Task added!")

def mark_done():
    view_tasks()
    try:
        task_no=int(input("Enter task number to mark as done:"))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]["done"]=True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no=int(input("Enter task number to mark as done:"))
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

while True:
    show_menu()
    choice=int(input("Choose an option (1-5):"))
    try:
        if choice == 1:
            view_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            ("Invalid option. Try again.")
    except ValueError:
            print("Enter a valid number.")
      
