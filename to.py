import os
from tabulate import tabulate

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip().split(",") for line in file.readlines()]
        return tasks
    else:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(",".join(task) + "\n")

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print(tabulate(tasks, headers=["Task", "Status"]))
    else:
        print("No tasks found!")

# Function to add a task
def add_task(tasks, task):
    tasks.append([task, "Incomplete"])

# Function to delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index!")

# Function to mark a task as complete
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index][1] = "Complete"
    else:
        print("Invalid task index!")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)

        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Complete")
        print("4. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            task_index = int(input("Enter task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to mark as complete: "))
            complete_task(tasks, task_index)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Quitting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
