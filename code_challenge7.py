buy =input("did you buy grocery? yes or no: ")

price = 250.00


if buy.lower() == "yes":
    print("item available:")
    print("-pork")
    print("-milk")
    print("-chicken")
    print("-beef")
    ans= print("answer the needed below")
    
else:
    print("error")

if buy.lower() == "yes":
    items = ["pork", "milk", "chicken", "beef"]
    price = 250.00 

    
    item = input("Name of the item: ").lower()

    if item in items:
        print("The price of the item is:", price)
        amount = int(input("Enter the amount: "))
        age = int(input("Enter your age: "))
    
        discount = round((price *0.052), 2)

        total = price - discount

        exc = amount - total

        tax = round((price * 0.123), 2)
        total2 = price + tax
        exc2 = amount - total
        if age >= 60 and amount:
            print("hi customer, you purchased a", item, "with a price of 250.000 discounted by 5.2% which is", discount )
            print(f"total of: {total},")
            print("amount given: " , amount)
            print("change: " , exc )

        elif age < 60 and amount:
            print("hi customer, you purchased a", item, "with a price of 250.000 plus 12.3% tax which is", tax )
            print("total of: ", total2)
            print("amount given: " , amount)
            print("change: " , exc2)

else:
    print("error")