list_py = [1,2,3,4]

sumVal = 0
for i in range(len(list_py)):
    sumVal += list_py[i]

print("Sum of elements in list_py:", sumVal)
print(sum(list_py))  # Using built-in sum function