import json
import os

FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("✅ Task added!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["done"] else " "
        print(f"{i}. [{status}] {t['task']}")

# Mark task as done
def mark_done(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("✅ Task marked as done!")
    else:
        print("Invalid task number!")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        save_tasks(tasks)
        print("✅ Task deleted!")
    else:
        print("Invalid task number!")

# Main program menu
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("Please type something.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to mark done: "))
                mark_done(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
