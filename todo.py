tasks = []

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    elif choice == '3':
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed.")
        else:
            print("Invalid number.")

    elif choice == '4':
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice!")
