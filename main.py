import os
import json

expenses = []

def add_expense():
    #This function should collect user input, save to the expenses ds and save it to the json file
    name = input("Enter the name of the expense: ")
    amount = float(input("Enter the amount spent on the item: "))
    
    expenses.append({"name": name, "amount": amount})
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
   
def view_expenses():
    #This function is able to read the expenses from the json file and print it in a readable format
    for (index, expense) in enumerate(expenses):
        print(f"{index + 1}. {expense['name']} - ${expense['amount']}")
    
try:
    #This try/except block checks if the expenses.json file exists, if it does it loads the data into the expenses ds, if not it creates an empty json file to store the data in the future
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            expenses.extend(json.load(file))
    else:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)

except Exception as e:
    print(e)

while True:
    #This while loop serves as the menu of the CLI expense tracker
    print("Welcome to the Expense Tracker!")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Exit \n")
        
    choice = input("Please select an option: \n")
        
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option, please try again.")
