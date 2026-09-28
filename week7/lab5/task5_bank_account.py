# task5_bank_account.py

balance = 1000
def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount deposited successfully.")
def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient funds.")
while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)
        print("Current Balance:", balance)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)
        print("Current Balance:", balance)
    elif choice == "3":
        print("Current Balance:", balance)
    elif choice == "4":
        print("Thank you for using the bank system.")
        break
    else:
        print("Invalid choice. Please try again.")

'''output:
--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter deposit amount: 10000
Amount deposited successfully.
Current Balance: 11000.0

--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 2
Enter withdrawal amount: 2000
Amount withdrawn successfully.
Current Balance: 9000.0

--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current Balance: 9000.0

--- Bank Account Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 4
Thank you for using the bank system.'''
