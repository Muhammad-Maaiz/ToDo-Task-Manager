# TO DO Task Manager:

print("***WELCOME to our TO DO Task Manager ***".center(120))
tasks = []
done_tasks = []

def display_menu():
    print("Main Menu:\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. View done Tasks")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(index, task)

def mark_task_done():
    view_tasks()
    index = int(input("Enter the index of the task to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        completed_task = tasks.pop(index)
        done_tasks.append(completed_task)
        print(f"Task '{completed_task}' marked as done!")
    else:
        print("Invalid task index.")

def view_done_tasks():
    if not done_tasks:
        print("No done tasks.")
    else:
        print("Completed Tasks:")
        for index, task in enumerate(done_tasks, start=1):
            print(index, task)

def delete_task():
    view_tasks()
    index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        mark_task_done()
    elif choice == 4:
        view_done_tasks()
    elif choice == 5:
        delete_task()
    elif choice == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")