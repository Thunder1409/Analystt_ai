def main():
    while True:
        username = input("Enter database username: ")
        password = input("Enter database password: ")

        todo_list = TodoList(username, password)

        # Attempt to connect to the database
        try:
            todo_list.connect_to_database()
            break  # If successful, break out of the loop
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            print("Please check your username and password and try again.")

    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. See tasks")
        print("4. Mark task as complete")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print("\n")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to delete: ")
            todo_list.delete_task(task)
        elif choice == '3':
            todo_list.see_tasks()
        elif choice == '4':
            task = input("Enter task to mark complete: ")
            todo_list.mark_complete(task)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
