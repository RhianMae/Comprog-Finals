balance = 5000 

while True:
    print("\n1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to withdraw: "))

        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)

    elif choice == "2":
        print("Your current balance is:", balance)

    elif choice == "3":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Please try again.")