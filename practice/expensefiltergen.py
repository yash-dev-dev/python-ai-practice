expenses = [
    {"category": "food", "amount": 200},
    {"category": "travel", "amount": 500},
    {"category": "food", "amount": 150},
]
def filter_expenses(expenses, category):
    for expense in expenses:
        if expense["category"]==category:
            yield expense

stall=filter_expenses(expenses,"travel")
for value in stall:
   print(value)        