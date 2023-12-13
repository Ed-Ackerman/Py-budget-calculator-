# budget.py
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description}{' '*(23-len(description))}{amount}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [(c.category, sum(item['amount'] for item in c.ledger if item['amount'] < 0)) for c in categories]
    total_spent = sum(spending for category, spending in spendings)

    for i in range(100, -1, -10):
        chart += f"{i:3}|"
        for category, spending in spendings:
            percentage = spending / total_spent * 100 if total_spent > 0 else 0
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    chart += "    ----------\n"

    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            chart += category.category[i] if i < len(category.category) else " "
            chart += "  "
        chart += " \n"

    return chart.rstrip()
