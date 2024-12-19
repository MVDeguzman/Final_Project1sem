gold=0
miner= input("Hi, what is ypour name:")
isgold= input("is the mineral gold?")

if isgold == "yes":
    gold+=1 
    print(f" Hi {miner}, Your total number of gold is {gold}")
else:
    print(f"INVALID")
