def checkGratest(a,b,c):
    list = [a, b, c]
    gratest = list[0]
    for i in list:
        if i > gratest:
            gratest = i
    return gratest

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
gratest = checkGratest(a, b, c)
print(f"The gratest number is: {gratest}")