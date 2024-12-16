class Expense:
    def __init__(self, date, description, amount):
        # Initialize the date, description, and amount of the expense
        self.date = date
        self.description = description
        self.amount = amount

# multiple class expenses
class ExpenseTracker:
    def __init__(self):
        # Initialize list to the store expenses
        self.expenses = []

    def add_expense(self, expense):
        # Add expense to the list of expenses
        self.expenses.append(expense)
    
    def remove_expense(self, index):
        # If it is exist then remove expense otherwise print error message
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else: 
            print("Invalid expense index.")

    def view_expenses(self):
        # Display all expenses and total amount
        if len(self.expenses) == 0:
           # If there are no expenses, notify it
            print("No expenses found.")
        else: 
            # Print the list of expenses with details
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")
            
            # Calculate and print the total amount of all expenses
            total = sum(expense.amount for expense in self.expenses)
            print(f"\nTotal Expenses: ${total:.2f}")

    def calculate_percentage(self, first_value, second_value):
        # Calculate the percentage change between two values
        if second_value == 0:
            #If it's impossible to calculate, notify it
            print("Cannot calculate percentage.")
            return None
        # calculate percentage change
        percentage = ((second_value - first_value) / first_value) * 100
        return percentage

# Main function to interact with the expense tracker
def main(): 
    # Create tracker instance of the ExpenseTracker
    tracker = ExpenseTracker()

    # Start infinite loop for the menu
    while True:
        # Print the menu options
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Calculate Percentage")
        print("5. Exit")

        # Get user's choice
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Option to add an expense
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            # Create Expense and add it to the tracker
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully.")

        elif choice == "2":
            # Option to remove expense
            index = int(input("Enter the expense index to remove: ")) - 1
            # Remove the specified index
            tracker.remove_expense(index)
        elif choice == "3":
            # Option to view all expenses
            tracker.view_expenses()
        elif choice == "4":
                # Input the first and second values
                first_value = float(input("Enter the first number : "))
                second_value = float(input("Enter the second number: "))
                # Calculate and print the percentage
                percentage = tracker.calculate_percentage(first_value, second_value)
                if percentage is not None:
                    print(f"The percentage is {percentage:.2f}%")
        elif choice == "5":
            # exit the program
            print("Goodbye!")
            break
        else:
            # notify the invalid menu choices
            print("Invalid choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()

