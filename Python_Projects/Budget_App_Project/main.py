class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        result = self.category.center(30, "*") + "\n"

        for items in self.ledger:
            temp = f"{items['description'][:23]:23}{items['amount']:7.2f}"
            result += temp + "\n"

        result += "Total: " + str(self.get_balance())
        return result
        

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True
        return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

def create_spend_chart(categories):
    spend = []
    for category in categories:
        temp = 0
        for items in category.ledger:
            if items['amount'] < 0:
                temp += abs(items['amount'])
        spend.append(temp)

    total = sum(spend)
    percentage = [i/total * 100 for i in spend]

    result = "Percentage spent by category"
    for i in range(100, -1, -10):
        result += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            if j > i:
                result += " o "
            else:
                result += "   "
        result += " "
    result += "\n    ----------" 

    category_length = []
    for category in categories:
        category_length.append(len(category.category))
        max_length = max(category_length)
        
    for i in range(max_length):
        result += "\n    "
        for j in range(len(categories)):
            if i < category_length[j]:
                result += " " + categories[j].category[i] + " "
            else:
                result += "   "
        result += " "
    return result

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
