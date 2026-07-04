total = 0

print("===== Expense Tracker =====")

while True:
    user_input = input("Enter an expense (or type 'exit' to finish): ")

    if user_input.lower() == "exit":
        break

    expense = float(user_input)
    total += expense

    print(f"Current Total: {total}")

print("\n===== Summary =====")
print(f"Total Spent: {total}")
print("Thank you for using the Expense Tracker!")