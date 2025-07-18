list = ["Rakesh", "Nitish", "After", "Rohon", "Rijwan"]

name = input("enter your name: ")

found = False
for i in range(len(list)):
    if(name == list[i]):
        found = True
        break

if(found):
    print("it found")
else:
    print("it not found")





#     if name in names:
#     print("It is found.")
# else:
#     print("It is not found.")