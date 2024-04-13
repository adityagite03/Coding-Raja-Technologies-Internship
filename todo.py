import json
import os
from datetime import datetime

# Function to load tasks from file
def load_tasks(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks, file_name):
    with open(file_name, 'w') as file:
        json.dump(tasks, file)

# Function to add a task
def add_task(tasks, title, priority, due_date):
    tasks.append({'title': title, 'priority': priority, 'due_date': due_date, 'completed': False})
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def mark_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("\nTask List:")
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i + 1}. {task['title']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

# Main function
def main():
    tasks = load_tasks('tasks.json')

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, priority, due_date)
        elif choice == '2':
            index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, index)
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: ")) - 1
            mark_completed(tasks, index)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks, 'tasks.json')
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()