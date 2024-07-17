# Budget Categories and Spend Chart

A brief description of what this project does and who it's for

## Overview

This project includes a `Category` class for managing transactions within different budget categories and a `create_spend_chart` function to visualize spending percentages across these categories.

## Category Class

The `Category` class allows you to track deposits, withdrawals, and transfers between budget categories. It provides methods for managing transactions and checking balances.

### Class Methods:

- **init(category):** Initializes a new budget category with a specified name.

- **deposit(amount, description=""):** Records a deposit transaction with an optional description.

- **withdraw(amount, description=""):** Records a withdrawal transaction if sufficient funds are available.

- **transfer(amount, category):** Transfers funds to another category if sufficient funds are available.

- **get_balance():** Returns the current balance of the category.

- **check_funds(amount):** Checks if there are sufficient funds available for a specified amount.

## Features

- **Transaction Management:** Tracks deposits, withdrawals, and transfers accurately within each category.

- **Balance Checking:** Provides methods to check the current balance and verify sufficient funds before transactions.

- **Category Transfer:** Allows for seamless transfer of funds between different budget categories.

- **String Representation:** Utilizes `__str__` method to display a formatted summary of transactions and current balance.

## Example Usage

    food = Category("Food")
    food.deposit(1000, "Initial deposit")
    food.withdraw(10.15, "Groceries")
    food.withdraw(15.89, "Restaurant and more food for dessert")

    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)

    auto = Category("Auto")
    auto.deposit(1000, "Initial deposit")
    auto.withdraw(15)

    print(food)
    print(clothing)
    print(auto)

### Output:

    *************Food*************
    Initial deposit          1000.00
    Groceries                  -10.15
    Restaurant and more foo...  -15.89
    Total: 973.96

    ***********Clothing***********
    Transfer to Clothing       -50.00
    withdrawal                 -25.55
    withdrawal                -100.00
    Total: -175.55

    *************Auto*************
    Initial deposit          1000.00
    withdrawal                 -15.00
    Total: 985.00

## create_spend_chart Function

The `create_spend_chart` function generates a visual representation of spending percentages across multiple budget categories.

### Function Parameters:

- **categories:** A list of Category objects.

### Features:

- **Percentage Calculation:** Computes spending percentages for each category based on total withdrawals.

- **Visual Chart:** Creates a bar chart showing spending percentages with ASCII characters.

## Example Usage:

        print(create_spend_chart([food, clothing, auto]))

### Output:

        Percentage spent by category
        100|          
         90|          
         80|          
         70|          
         60|       o  
         50|       o  
         40|       o  
         30|       o  
         20| o     o  
         10| o     o  
          0| o  o  o  
            ----------
             F  C  A  
             o  l  u  
             o  o  t  
             d  t  o  
             h     
             i     
             n     
             g     

## Tests

1. The deposit method should create a specific object in the ledger instance variable.
2. Calling the deposit method with no description should create a blank description.
3. The withdraw method should create a specific object in the ledger instance variable.
4. Calling the withdraw method with no description should create a blank description.
5. The withdraw method should return True if the withdrawal took place.
6. Calling food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') should return a balance of 854.33.
7. Calling the transfer method on a category object should create a specific ledger item in that category object.
8. The transfer method should return True if the transfer took place.
9. Calling transfer on a category object should reduce the balance in the category object.
10. The transfer method should increase the balance of the category object passed as its argument.
11. The transfer method should create a specific ledger item in the category object passed as its argument.
12. The check_funds method should return False if the amount passed to the method is greater than the category balance.
13. The check_funds method should return True if the amount passed to the method is not greater than the category balance.
14. The withdraw method should return False if the withdrawal didn't take place.
15. The transfer method should return False if the transfer didn't take place.
16. Printing a Category instance should give a different string representation of the object.
17. create_spend_chart should print a different chart representation. Check that all spacing is exact.

## Credits

This project is the certificate project from Freecodecamp.