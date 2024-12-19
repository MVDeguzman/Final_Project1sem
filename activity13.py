
n1 = eval(input("Enter a number: "))
n2 = 1
for x in range(n1, 0, -1):
        print(x)
        n2 *= x
print(f"The Factorial of {n1} is {n2}")
