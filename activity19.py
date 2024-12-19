
contin = True
count = 0

while contin == True:
        name = input("Enter a name: ").upper().strip()

        if name == "STOP":
            print("The loop has now stopped")
            print(f"You have entered {count} number of names")
            break

        else:
            count += 1
            continue


