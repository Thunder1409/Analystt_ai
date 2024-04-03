import mysql.connector
from datetime import datetime


def create_database_and_table(username, password):
    try:
        conn = mysql.connector.connect(host="localhost", user=username, password=password)
        cursor = conn.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS expense_tracker")
        conn.database = "expense_tracker"

        # Create the table if it doesn't exist
        cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            amount FLOAT,
                            category VARCHAR(50),
                            date DATE
                          )""")

        conn.commit()
        print("Database and table created...")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


def add_expense(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database="expense_tracker"
        )
        cursor = conn.cursor()

        while True:
            try:
                amount = float(input("Enter the amount spent: "))
                if amount > 0:
                    break
                else:
                    print("Please enter an amount greater than 0.")
            except ValueError:
                print("Please enter a valid amount.")

        print("\nSelect a category:")
        print("1. Food")
        print("2. Transportation")
        print("3. Shopping")
        print("4. Utilities")
        print("5. Entertainment")
        print("6. Other")

        category_choice = input("Enter the category number: ")
        categories = {
            '1': 'Food',
            '2': 'Transportation',
            '3': 'Shopping',
            '4': 'Utilities',
            '5': 'Entertainment',
            '6': 'Other'
        }

        category = categories.get(category_choice)
        if not category:
            category = "Other"

        current_date = datetime.now().date()

        cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)",
                       (amount, category, current_date))
        conn.commit()

        print("\nExpense of $%.2f added to category: %s" % (amount, category))
        print("Date of expense:", current_date)

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


def categorize_expenses(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database="expense_tracker"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        expenses = cursor.fetchall()

        if expenses:
            print("\nCategorized Expenses:")
            for category, total_amount in expenses:
                print(f"{category}: ${total_amount:.2f}")
        else:
            print("\nNo expenses found.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


def view_spending_patterns(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database="expense_tracker"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT date, SUM(amount) FROM expenses GROUP BY date")
        expenses = cursor.fetchall()

        if expenses:
            print("\nSpending Patterns Over Time:")
            for date, total_amount in expenses:
                print(f"{date}: ${total_amount:.2f}")
        else:
            print("\nNo expenses found.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


def main():
    while True:
        username = input("Enter database username: ")
        password = input("Enter database password: ")

        try:
            create_database_and_table(username, password)
            break  # If successful, break out of the loop
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            print("Please check your username and password and try again.")

    while True:
        print("\n1. Add expense")
        print("2. Categorize expenses")
        print("3. View spending patterns over time")
        print("4. Exit")
        choice = input("Enter your choice: ")
        print("")

        if choice == '1':
            add_expense(username, password)
        elif choice == '2':
            categorize_expenses(username, password)
        elif choice == '3':
            view_spending_patterns(username, password)
        elif choice == '4':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
