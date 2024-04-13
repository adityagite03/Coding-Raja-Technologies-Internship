import json
import os


# Function to load existing data from file
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}


# Function to save data to file
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)


# Function to add income
def add_income(data, amount):
    data['income'] += amount
    save_data(data, 'budget_data.json')
    print("Income added successfully.")


# Function to add expense
def add_expense(data, category, amount):
    data['expenses'].append({'category': category, 'amount': amount})
    save_data(data, 'budget_data.json')
    print("Expense added successfully.")


# Function to calculate remaining budget
def calculate_budget(data):
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    return remaining_budget


# Function to analyze expenses by category
def analyze_expenses(data):
    expense_by_category = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        expense_by_category[category] = expense_by_category.get(category, 0) + amount
    return expense_by_category


# Main function
def main():
    budget_data = load_data('budget_data.json')

    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the income amount: "))
            add_income(budget_data, amount)
        elif choice == '2':
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            add_expense(budget_data, category, amount)
        elif choice == '3':
            remaining_budget = calculate_budget(budget_data)
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == '4':
            expense_analysis = analyze_expenses(budget_data)
            print("\nExpense Analysis:")
            for category, amount in expense_analysis.items():
                print(f"{category}: ${amount:.2f}")
        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
