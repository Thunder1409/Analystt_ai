class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task.lower())
        print(f"Task '{task}' added.")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task.lower())
            print(f"Task '{task}' deleted.")
        else:
            print(f"Task '{task}' not found.")

    def see_tasks(self):
        if self.tasks:
            print("\nTasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("\nNo tasks.")

    def mark_complete(self, task):
        if task in self.tasks:
            print(f"Task '{task}' marked as complete.")
            self.delete_task(task.lower())
        else:
            print(f"Task '{task}' not found.")

def main():
    todo_list = TodoList()

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
