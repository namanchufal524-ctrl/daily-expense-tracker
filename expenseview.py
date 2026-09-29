def searchcategory(expenses):
    print("Search by Category")
    if len(expenses)==0:
        print("No expenses found.")
        return
    category=input("Enter category to search: ")
    found=False
    for expense in expenses:
        if expense["category"].lower()==category.lower():
            print(expense["date"],"|",expense["category"],"|",expense["amount"])
            found=True
    if found==False:
        print("No expenses found in this category.")

def categorytotal(expenses):
    print("Categoryw ise Total")
    if len(expenses)==0:
        print("No expenses found.")
        return
    category=input("Enter category: ")
    total=0
    for expense in expenses:
        if expense["category"].lower()==category.lower():
            total=total+expense["amount"]
    print("Total spent on",category,"=",total)
