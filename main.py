# main.py
from budget import Category, create_spend_chart

def main():
    # Initialize an empty list to store budget categories
    budget_categories = []

    while True:
        print("\n1. Create Category\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Create Spend Chart\n6. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Create a new category
            category_name = input("Enter the name of the category: ")
            budget_category = Category(category_name)
            budget_categories.append(budget_category)
            print(f"Category '{category_name}' created!")

        elif choice == '2':
            # Deposit money into a category
            display_categories(budget_categories)
            category_index = int(input("Enter the category index to deposit into: "))
            deposit_amount = float(input("Enter the deposit amount: "))
            description = input("Enter a description (optional): ")
            budget_categories[category_index].deposit(deposit_amount, description)
            print("Deposit successful!")

        elif choice == '3':
            # Withdraw money from a category
            display_categories(budget_categories)
            category_index = int(input("Enter the category index to withdraw from: "))
            withdraw_amount = float(input("Enter the withdrawal amount: "))
            description = input("Enter a description (optional): ")
            success = budget_categories[category_index].withdraw(withdraw_amount, description)
            if success:
                print("Withdrawal successful!")
            else:
                print("Insufficient funds!")

        elif choice == '4':
            # Transfer money between categories
            display_categories(budget_categories)
            source_index = int(input("Enter the source category index: "))
            destination_index = int(input("Enter the destination category index: "))
            transfer_amount = float(input("Enter the transfer amount: "))
            success = budget_categories[source_index].transfer(transfer_amount, budget_categories[destination_index])
            if success:
                print("Transfer successful!")
            else:
                print("Insufficient funds for transfer!")

        elif choice == '5':
            # Create and display spend chart
            chart = create_spend_chart(budget_categories)
            print(chart)

        elif choice == '6':
            # Exit the program
            print("Exiting the budget app. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def display_categories(categories):
    # Display categories
    print("Categories:")
    for i, category in enumerate(categories):
        print(f"{i}. {category.category}")

if __name__ == "__main__":
    main()
