def inchesToCm(i):
    cm = i * 2.54
    return cm

i = float(input("Enter the length in inches: "))
result = inchesToCm(i)
print(f"{i} inches is equal to {result} centimeters.")