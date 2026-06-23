def tasks():
    task = []

    print("\n===== WELCOME TO THE TASK MANAGEMENT APP =====")

    try:
        total_task = int(input("Enter how many tasks you want to add: "))

        for i in range(1, total_task + 1):
            task_name = input(f"Enter task {i}: ")
            task.append(task_name)

    except ValueError:
        print("Please enter a valid number.")
        return

    while True:
        print("\n===== TASK MENU =====")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Add Task
        if operation == 1:
            add = input("Enter task to add: ")
            task.append(add)
            print(f"✓ Task '{add}' added successfully.")

        # Update Task
        elif operation == 2:
            old_task = input("Enter task name to update: ")

            if old_task in task:
                new_task = input("Enter new task name: ")
                index = task.index(old_task)
                task[index] = new_task
                print(f"✓ Task updated to '{new_task}'.")
            else:
                print("✗ Task not found.")

        # Delete Task
        elif operation == 3:
            del_task = input("Enter task name to delete: ")

            if del_task in task:
                task.remove(del_task)
                print(f"✓ Task '{del_task}' deleted successfully.")
            else:
                print("✗ Task not found.")

        # View Tasks
        elif operation == 4:
            if len(task) == 0:
                print("No tasks available.")
            else:
                print("\n===== YOUR TASKS =====")
                for i, t in enumerate(task, start=1):
                    print(f"{i}. {t}")

        # Exit
        elif operation == 5:
            print("Closing the program...")
            print("Thank you for using Task Management App!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


tasks()
