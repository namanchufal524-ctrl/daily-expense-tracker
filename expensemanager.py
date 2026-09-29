def addexpense(expenses):
    print(" Add Expenses ")
    amount=float(input("Enter amount: "))
    category=input("Enter category (Food, Travel, Shopping, etc.): ")
    date=input("Enter date (DD-MM-YYYY): ")
    expense={"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    print("Expense added successfully!!!")

def viewexpenses(expenses):
    print("All Expenses")
    if len(expenses)==0:
        print("No expenses found.")
        return

    number=1
    for expense in expenses:
        print(number,"|",expense["date"],"|", expense["category"],"|",expense["amount"])
        number = number + 1

def deleteexpense(expenses):
    print("Delete Expense")
    if len(expenses)==0:
        print("No expenses to delete.")
        return 

    viewexpenses(expenses)
    choice=int(input("Enter the number of the expense to delete: "))
    if choice >= 1 and choice <= len(expenses):
        expenses.pop(choice - 1)
        print("Expense deleted successfully!!!")
    else:
        print("Invalid number.")
