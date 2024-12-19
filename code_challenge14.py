tuloy = True
total = 0
while tuloy == True:
    num = input("Please enter a number --> ")

    if num == "0":
        print("Loop has terminated")
        print(f"The sum of all the numbers given is {total}")
        break
        tuloy = False
    else:
        num=eval(num)
        total += num
        continue