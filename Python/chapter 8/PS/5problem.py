def printPattern(n):
    for i in range(1, n + 1):
        print("*" * (n + 1 - i), end="")
        print("")

n = int(input("Enter the number of rows for the pattern: "))
printPattern(n)