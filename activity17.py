column= eval(input("enter a number--->"))
for x in range(1,11):
    for y in  range(1, column + 1):
        print(f"{x} x {y} = {x * y}", end= "\t")
    print()
