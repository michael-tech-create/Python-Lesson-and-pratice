balance = 5000

while True:
    print("\n=== Welcome to Msmart Bank ===")
    print("1. Check balance")
    print("2. Withdraw cash")
    print("3. Deposit funds")
    print("4. Transfer funds")
    print("5. Exit")

    choice = int(input("Enter your option: "))

    # CHECK BALANCE
    if choice == 1:
        print("Your balance is:", balance)

    # WITHDRAW CASH
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print("Withdrawal approved")
            print("New balance:", balance)

    # DEPOSIT FUNDS
    elif choice == 3:
        amount = int(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid amount!")
        else:
            balance += amount
            print("Deposit successful")
            print("New balance:", balance)

    # TRANSFER FUNDS
    elif choice == 4:
        amount = int(input("Enter transfer amount: "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Transaction failed! Insufficient balance.")
        else:
            balance -= amount
            print("Transfer successful")
            print("New balance:", balance)

    # EXIT
    elif choice == 5:
        print("Thanks for banking with us!")
        break

    # INVALID OPTION
    else:
        print("Invalid option. Try again.")