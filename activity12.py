# for i in range(10, 1, -1):
#     print(i)
print("Enter 10 number \n------------------\n ")

n1 = 0
odd = 0
even = 0 
for i in range(1, 11):
    n2 = eval(input(f"Enter a number {i}: "))
    n1 += n2
    if n2 % 2 == 0:
        even += n2
    else:
        odd += n2

print(f"The total of the number you entered is {n1} ")
print(f"The total of the EVEN number you entered is {even} ")
print(f"The total of the ODD you entered is {odd} ")

