def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n📭 No tasks found.\n")
        return
    print("\n📝 Your To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "🔹"
        print(f"{i}. {t['task']} {status}")
    print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("✅ Task added successfully.\n")
    else:
        print("⚠️ Task cannot be empty.\n")

def mark_done(tasks):
    """Mark a task as done."""
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("🎉 Task marked as complete!\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Enter a valid number.\n")

def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Deleted: {removed['task']}\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Enter a valid number.\n")

def main():
    tasks = []  # tasks are stored in memory only

    while True:
        print("==== 🧠 To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... All tasks will be cleared. Goodbye!")
            break
        else:
            print("⚠️ Invalid option, try again.\n")

if __name__ == "__main__":
    main()
