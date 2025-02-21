class ATM:
    def __init__(self,name,initial_balance,pin):
        self.name = name
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history =[]

    def validate_pin(self, entered_pin):
        return self.pin ==entered_pin

    def deposit(self,amount):
        self.balance += amount
        self.transaction_history.append(
            {"Type": "deposit","amount":amount, "balance": self.balance}
        ) 
        return self.balance

    def view_transaction_history (self):
        if not self.transaction_history:
            print("no transactions available.")
        else:
             print("\ntransaction history:")
        for index, transaction in enumerate(self.transaction_history, start=1):
            print(
                f"{index}.{transaction['Type']} - Amount:{transaction['amount']} - balance:{transaction['balance']}"
            )
name = input("Enter Name: ")
initial_balance = float(input("Enter Your Balance: "))
while initial_balance <= 0:
    print("Balance Should be greater than 0.")
    initial_balance = float(input("Enter Your Balance: "))

pin = input("Set Your PIN (4-digit): ")
while len(pin) != 4 or not pin.isdigit():
    print("Invalid PIN. Enter a 4-digit numeric PIN.")
    pin = input("Set Your PIN (4-digit): ")


atm=ATM(name, initial_balance, pin)
while True:
    entered_pin = input("enter your pin :")
    if atm.validate_pin(entered_pin):
        print(f"welcome {atm.name}!")
        while True:
            print("\noptions:")
            print("1.deposit")
            print("2.withdrawl")
            print("3.view transaction history")
            print("4.exit")
            choice = input("enter your choice:")
            if choice == "1":
                deposit_amount = float(input("enter the amount to deposit:"))
                atm.deposit(deposit_amount)
                print(f"your current balance is:{atm.balance}")
            elif choice =="2":
                withdrawl_amount = float(input("enter the amount to withdrawl:"))
                atm.withdrawl(withdrawl_amount)
                print(f"your current balance is:{atm.balance}")
            elif choice =="3":
                atm.view_transaction_history()
            elif choice =="4":
                print("BYE!")
                break
            else:
                print("invalid choice.please try again.")
        else:     
            print("incorrect pin. please try again.")      