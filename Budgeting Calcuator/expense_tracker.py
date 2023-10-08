from expense import Expense  # Import the Expense class from the expense module.

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"  # Define the path to the expense file.
    budget = 2000  # Set the budget for the month.

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read the file and summarize all expenses.
    summarize_expense(expense_file_path, budget)

# User input for expense class
def get_user_expense():
    print(f"Getting User Expense!")
    expense_name = input("Enter name of expense: ") 
    expense_amount = float(input("Enter Expense Amount: "))
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]
    # While loop for assigning a number to each expense category
    while True:
        print("Select Category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name}")
        
        # Index for each category
        value_range = f"[1 - {len(expense_categories)}]: "
        
        #Stores user input of category number
        selected_index = int(input(f"Enter a category number: {value_range} ")) - 1

        #if statement for checking if category number inputted is within range
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index] # Make sense of the index of the expense category
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount) # To declare a new variable holding one instance of the class
            return new_expense
        else:
            print("Invalid category. Please try Again") #if inputted expense category is not within range of 1 to 5 this will print
        break


def save_expense_to_file(expense, expense_file_path):
    # Open the expense file in "append" mode and write the expense information.
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarize_expense(expense_file_path, budget):
    print(f"Summarizing expenses!")
    expenses = []

    # Read the expense file and create Expense objects.
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")

            # Create Expense objects from the stored data.
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {} # declaring a dictionary

    # Calculate total expenses by category.
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount # First instance where categories are similar
        else:
            amount_by_category[key] = expense.amount # second instance where categories are not similar

    print("Expenses by categories: ") 
    for key, amount in amount_by_category.items(): # iterate through each key/category and print them on seprate lines
        print(f"   {key}: ${amount:.2f}") 

    total_spent = sum([expense.amount for expense in expenses]) # for every expense in the expenses, create a new list where each item in the list is equal to expenses amount
    print(f"Total spent ${total_spent:.2f} this month.")

    remaining_budget = budget - total_spent # Calculates remaining budget
    print(f"Budget remaining ${remaining_budget:.2f} this month.")


if __name__ == "__main__":
    main()