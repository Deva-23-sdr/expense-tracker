import csv
import os
from datetime import datetime

FILENAME = 'expenses.csv'

# Create CSV file with headers if not already present
def setup_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

# Add a new expense
def add_expense():
    date = input("Date (YYYY-MM-DD) [Enter for today]: ").strip()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    category = input("Category: ").strip()
    amount = input("Amount: ").strip()
    description = input("Description (optional): ").strip()

    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    print("Expense added!\n")

# View all recorded expenses
def view_expenses():
    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        print("No expenses found.\n")
        return

    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                print(f"{row[0]:<12} {row[1]:<15} {row[2]:<10} {row[3]}")
                print("-" * 50)
            else:
                print(f"{row[0]:<12} {row[1]:<15} ₹{float(row[2]):<10.2f} {row[3]}")
    print()

# Menu to navigate options
def main():
    setup_file()
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose (1-3): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
