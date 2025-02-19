name = input("Enter name: ")
initial_balance = float(input("Enter your balance: "))

while initial_balance <= 0:
    print("Balance should be greater than 0.")
    initial_balance = float(input("Enter your balance: "))

pin = input("Set your PIN (4 digits): ")
while len(pin) != 4 or not pin.isdigit():
    print("Invalid PIN. Enter a 4-digit numerical PIN:")
    pin = input("Set your PIN (4 digits): ")

def validate_pin(stored_pin, entered_pin):
    return stored_pin == entered_pin

def deposit(balance, damount):
    balance += damount
    return balance 

def withdraw(balance, wamount):
    while wamount > balance:
        print("Withdrawal amount exceeds current balance.")
        wamount = float(input("Enter a valid withdrawal amount: "))
    balance -= wamount
    return balance

# MAIN PROGRAM
while True:
    re_entered_pin = input("Enter your PIN: ")
    
    if validate_pin(pin, re_entered_pin):
        print(f"Welcome, {name}!")
        
        while True:
            print("\nOptions:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                deposit_amount = float(input("Enter the amount to deposit: "))
                initial_balance = deposit(initial_balance, deposit_amount)
                print(f"Your current balance is: {initial_balance}")

            elif choice == "2":
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                initial_balance = withdraw(initial_balance, withdraw_amount)
                print(f"Your current balance is: {initial_balance}")

            elif choice == "3":
                print("BYE!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Incorrect PIN. Please try again.")
