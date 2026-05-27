tasks = []

while True:
    print("1 Add")
    print("2 List")
    print("3 Delete")
    print("4 Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("")

    elif choice == "2":
        print(tasks)
        print("")

    elif choice == "3":
        print(tasks)
        task = input("Task to delete: ")
        tasks.remove(task)
        print("")

    elif choice == "4":
        print("GoodBye")
        break

