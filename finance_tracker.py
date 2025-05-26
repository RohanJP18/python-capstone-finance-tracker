# functions
print("Wecome to the Personal Finance Tracker")
user_dict = {}

def add_expense():
    try:
        description = input("Enter expense description: ")
        if not description:
            raise ValueError("Description cannot be empty.")
        category = input("Enter category: ")
        if not category:
            raise ValueError("Category cannot be empty.")
        amount = float(input("Enter amount: "))
        expenses_tuple = (description, amount)
        if category in user_dict:
            user_dict[category].append(expenses_tuple)
        else:
            user_dict[category] = [expenses_tuple]
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input, please enter valid entry. ")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
def view_expense():
    if not user_dict:
        print("No expenses recorded yet.")
        return
    for key, value in user_dict.items():
        print(f"\n Category: {key}")
        for desc, amt in value:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary():
    if not user_dict:
        print("No expenses to summarize.")
        return
    print("\nSummary:")
    for key, value in user_dict.items():
        total = sum(amount for _, amount in value)
        print(f"{key}: ${total:.2f}")
    pass

# intro code


while True:
        select = input("\n What would you like to do? \n " \
        "1. Add Expense \n" \
        "2. View All Expenses \n" \
        "3. View Summary \n" \
        "4. Exit \n" \
        "Choose an option: " )

        if select == "1":
            add_expense()
        elif select == "2":
            view_expense()
        elif select == "3":
            view_summary()  
        elif select == "4":
            break
        else:
            print("oh NO! please enter one of the valid choices")
           


# bye!
print("Goodbye!")