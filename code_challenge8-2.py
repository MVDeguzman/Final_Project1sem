numbers = 0

for i in range(10):
    number = int(input("Enter number " + str(i+1) + ": "))
    numbers.append(number)

sum_of_numbers = sum(numbers)

print("The sum of the numbers is:", sum_of_numbers)
