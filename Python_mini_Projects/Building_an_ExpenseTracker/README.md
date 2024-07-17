# Expense Tracker

This program tracks expenses and allows you to manage them based on categories.

## Overview

The Expense Tracker allows users to:

- Add expenses with specific amounts and categories.
- List all recorded expenses.
- Calculate the total expenses.
- Filter expenses by category.

## Features

- **Add Expense:** Record new expenses with amounts and categories.
- **List Expenses:** Display all recorded expenses.
- **Total Expenses:** Calculate the total amount spent.
- **Filter by Category:** View expenses filtered by a specific category.

## Getting Started
### Prerequisites
- Python 3.x
### Installation
No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Run the program:

        python expense_tracker.py

2. Follow the prompts to manage your expenses:

- Enter the amount and category to add a new expense.
- Choose options to list all expenses, calculate total expenses, filter expenses by category, or exit the program.

## Example

        # Example usage of the Expense Tracker program

        def add_expense(expenses, amount, category):
            expenses.append({'amount': amount, 'category': category})
    
        def print_expenses(expenses):
            for expense in expenses:
                print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
        def total_expenses(expenses):
            return sum(map(lambda expense: expense['amount'], expenses))
    
        def filter_expenses_by_category(expenses, category):
            return filter(lambda expense: expense['category'] == category, expenses)
    
        def main():
            expenses = []
            while True:
                print('\nExpense Tracker')
                print('1. Add an expense')
                print('2. List all expenses')
                print('3. Show total expenses')
                print('4. Filter expenses by category')
                print('5. Exit')
       
            choice = input('Enter your choice: ')

            if choice == '1':
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                add_expense(expenses, amount, category)

            elif choice == '2':
                print('\nAll Expenses:')
                print_expenses(expenses)
    
            elif choice == '3':
                print('\nTotal Expenses: ', total_expenses(expenses))
    
            elif choice == '4':
                category = input('Enter category to filter: ')
                print(f'\nExpenses for {category}:')
                expenses_from_category = filter_expenses_by_category(expenses, category)
                print_expenses(expenses_from_category)
    
            elif choice == '5':
                print('Exiting the program.')
                break

        if __name__ == "__main__":
            main()

## Credits

- This project is part of my coursework for Freecodecamp and contributes to my certificate project.
- **Hans Peter Luhn:** Developer of the Luhn algorithm used for credit card number validation.