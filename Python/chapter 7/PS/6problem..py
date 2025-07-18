num = int(input("Enter a number: "))

pro = 1
for i in range(1, num + 1):
    pro *= i

print(f"The product of numbers from 1 to {num} is {pro}")