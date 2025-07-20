def nNatural(n):
    if n <= 0:
        return 0
    return n + nNatural(n - 1)


n = int(input("Enter a number: "))
result = nNatural(n)
print(f"The sum of the first {n} natural numbers is: {result}")