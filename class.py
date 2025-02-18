name = input("Enter Name: ")
initial_balance = float(input("Enter Your Balance: "))

# Ensure initial balance is greater than 0
while initial_balance <= 0:
    print("Balance should be greater than 0.")
    initial_balance = float(input("Enter your balance again: "))

# PIN validation
pin = input("Enter your PIN: ")
while len(pin) != 4 or not pin.isdigit():
    print("Invalid PIN! Enter a 4-digit PIN (numbers only).")
    pin = input("Enter your PIN: ")

# Main loop for banking operations
while True:
    print("\n1. Deposit")
    print("2. Withdrawal")
    print("3. Exit")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        deposit = float(input("Enter your deposit amount: "))
        initial_balance += deposit
        print(f"Balance after deposit: {initial_balance}")

    elif choice == 2:
        withdrawal = float(input("Enter withdrawal amount: "))
        while withdrawal > initial_balance:
            print("Withdrawal amount should be less than or equal to the available balance.")
            withdrawal = float(input("Enter withdrawal amount: "))
        initial_balance -= withdrawal
        print(f"Balance after withdrawal: {initial_balance}")

    elif choice == 3:
        print("Thanks for visiting!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
