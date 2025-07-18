list = []

for i in range(4):
    num = int(input("enter a number: "))
    list.append(num)

print("The numbers you entered are:", list)

max_num = list[0]
for i in range(len(list)):
    if list[i] > max_num:
        max_num = list[i]

print("The maximum number is:", max_num)