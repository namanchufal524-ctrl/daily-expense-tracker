def totalspending(expenses):
    total=0
    for expense in expenses:
        total=total+expense["amount"]
    return total

def numberofexpenses(expenses):
    return len(expenses)

def averageexpense(expenses):
    if len(expenses)==0:
        return 0
    return totalspending(expenses)/len(expenses)

def highestexpense(expenses):
    if len(expenses)==0:
        return None
    highest=expenses[0]
    for expense in expenses:
        if expense["amount"]>highest["amount"]:
            highest=expense
    return highest

def showanalysis(expenses):
    print("Expense Analysis")
    if len(expenses)==0:
        print("No expenses found.")
        return
    print("Total spending:", totalspending(expenses))
    print("Number of expenses:", numberofexpenses(expenses))
    print("Average expense:", averageexpense(expenses))

    highest=highestexpense(expenses)
    print("Highest expense:", highest["amount"], "on", highest["category"], "(", highest["date"], ")")
