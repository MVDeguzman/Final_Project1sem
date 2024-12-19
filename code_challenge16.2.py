balance = 0 

def create_account(name, initial_deposit = 0):
    Account_name = name
    b = 0
    b = initial_deposit
    balance = b
    print(f"BANK ACCOUNT CREATE FOR {Account_name} WITH INITIAL DEPOSIT OF {balance}")

def check_balance():
    global balance
    print(f"CURRENT BALANCE IS {balance}")



def get_denomination(amount):
    d1 = amount // 1000
    depo1 = amount % 1000
    
    d2 = amount // 500
    depo2 = depo1 % 500
    
    d3 = amount // 200
    depo3 = depo2 % 200
    
    d4 = amount // 100
    depo4 = depo3 % 100
    
    d5 = amount // 50
    depo5 = depo4 % 50
    
    d6 = amount // 20
    depo6 = depo5 % 20
    
    d7 = amount // 10
    depo7 = depo6 % 10
    
    d8 = amount // 5
    depo8 = depo7 % 5
    
    d9 = amount // 1
    depo9 = depo8 % 1

    print(f"{d1} - 1000")
    print(f"{d2} - 500")
    print(f"{d3} - 200")
    print(f"{d4} - 100")
    print(f"{d5} - 50")
    print(f"{d6} - 20")
    print(f"{d7} - 10")
    print(f"{d8} - 5")
    print(f"{d9} - 1")


def deposit():
    global balance
    balance += amount
    print(f"Deposited {amount}. New balance is {balance}")

def withdraw():
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}. New balance is {balance}")
    else:
        print("Insufficient funds")



isCont = True

get_denomination(1378)
while isCont == True:
    print("WELCOME TO MY BANK SIMULATION PROGRAM")
    print("=====================================")
    print("ENTER FROM THE OPTIONS BELOW")
    print("1 -- CREATE ACCOUNT")
    print("2 -- DEPOSIT")
    print("3 -- CHECK BALANCE")
    print("4 -- WITHDRAW")
    print("5 -- EXIT")

    choice = input("Enter your choice -- > ")

    if choice == "1":
        print("BANK APPLICATION FORM")
        name = input("Please Enter Your FULL NAME --> ")
        print("INITIAL DEPOSIT IS A REQUIREMENT PHP100 MAINTAINING BALANCE")
        amount = int(input("Enter Amount to Deposit --> "))
        create_account(name, amount)
        print("ACCOUNT CREATED")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == "5":
        print("Exiting the bank simulation. Goodbye!")
        break