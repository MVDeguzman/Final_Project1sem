import os
name = input("Input your First name: ")
surname = input("Input your Surname: ")
age = input("Input your age: ")

def balance():
    global deposit
    deposit = eval(input(f"Hi {name}, Enter the amount you want to deposit in our bank: "))
    
balance()

while True:
    print(f"\nWelcome to our Banking System {name}!")
    action = input("1 - Do you want to deposit more? \n2 - Withdraw? \n3 - Check Balance \n4 - Stop \nPick an action: ").lower()
    if action == "1":
        deposit += eval(input("How much do you want to deposit: "))
        os.system('cls')
        continue

    elif action == "2":
        withdraw = eval(input("Enter the amount you want to withdraw: "))
        deposit -= withdraw
        print(f"You withdraw: ₱{withdraw}")
        
        if withdraw > deposit:
            print("You have Insufficient Balance.")
            os.system('cls')
            break
    
        else:
            continue 
    
    elif action == "3":
        os.system('cls')
        print(f"\n\nName: {name} {surname} \n Age: {age}")
        print(f"Current balance: ₱{deposit}.\n\n")
        continue
           
    elif action == "4":
        os.system('cls')
        print(f"\n\nYour current balance is ₱{deposit}.\n")
        isanglibo = 1000
        limangdaan = 500
        dalawangdaan = 200
        isangdaan = 100
        pipti = 50
        bente = 20
        sampo = 10
        lima = 5
        piso = 1   
             
        isanglibo = deposit // isanglibo
        sukli1 = deposit % 1000  
        limangdaan = sukli1 // limangdaan
        sukli2 = deposit % 500
        dalawangdaan = sukli2 // dalawangdaan
        sukli3 = deposit % 200
        isangdaan = sukli3 // isangdaan
        sukli4 = deposit % 100
        pipti = sukli4  // pipti
        sukli5 = deposit % 50
        bente = sukli5 // bente
        sukli6 = deposit % 20
        sampo = sukli6 // sampo
        sukli7 = deposit % 10
        lima = sukli7 // lima
        sukli8 = deposit % 5
        piso = sukli8 // piso
        sukli9 = deposit % 1
        zero = sukli9 // 1
        
        print(f"1000 = {isanglibo}\n500 = {limangdaan}\n200 = {dalawangdaan}\n100 = {isangdaan}\n50 = {pipti}\n20 = {bente}\n10 = {sampo}\n5 = {lima}\n1 = {piso}")
        print(f"\nThank you for using our bank {name}! \nPlease come again!")
        break
    
    else:
        print("Invalid action. Please try again.")
        break