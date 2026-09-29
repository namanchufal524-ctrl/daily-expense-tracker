import expensemanager
import expenseview
import expenseanalysis
expenses=[]

while True:
    print("DAILY EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search by Category")
    print("5. Category-wise Total")
    print("6. Expense Analysis")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice=="1":
        expensemanager.addexpense(expenses)
    elif choice=="2":
        expensemanager.viewexpenses(expenses)
    elif choice=="3":
        expensemanager.deleteexpense(expenses)
    elif choice=="4":
        expenseview.searchcategory(expenses)
    elif choice=="5":
        expenseview.categorytotal(expenses)
    elif choice=="6":
        expenseanalysis.showanalysis(expenses)
    elif choice=="7":
        print("Thank you for using Daily Expense Tracker!")
        break
    else:
        print("Invalid choice.Please enter a number from 1 to 7.")
