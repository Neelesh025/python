name=input("enter name:")
initial_balance= float(input("enter your balance:"))
while initial_balance <=0:
    print("balance should be greater than 0.")
    initial_balance= float(input("enter your balance:"))

pin = input("set your pin (4-digits):")
while len(pin) !=4 or not pin.isdigit():
    print("individual pin. enter a 4-digit numerical pin:")
    pin= input("set your pin(4-digits):")
def validate_pin(stored_pin,entered_pin):
    return stored_pin == entered_pin
def deposit(balance,damount):
    balance+=damount
    return balance 
def withdrawl(balance,wamount):
    while wamount>balance:
        print("withdrawl amount should not exceeded the current balance.")
        wamount=float(input("enter a valid withdrawl amount:"))
        balance-=wamount
        return balance
    #MAIN PROGRAM
    while True :
        re_rentered_pin=input("enter your pin:")
        if validate_pin(pin,re_rentered_pin):
            print(f"welcome{name}!")
            while True:
                print("\noptions:")
                print("1.deposit")
                print("2.withdrawl")
                print("3.exit")
                choice=input("enter your choice:")
                if choice=="1":
                    deposit_amount=float(input("enter the amount to deposit:"))
                    initial_balance=deposit(initial_balance,withdrawl_amount)
                    print(f"your current balance is:{initial_balance}")
                elif choice=="2":
                    withdrawl_amount=float(input("enter the amount to withdrawl:"))
                    initial_balance=withdrawl(initial_balance,withdrawl_amount)
                    print(f"your current balance is:{initial_balance}")
                elif choice=="3":
                    print("BYE!")
                    break
                else:
                    print("invalid choice.please try again.")
            else:
                print("incorrect pin.please try again.")
                
                                    