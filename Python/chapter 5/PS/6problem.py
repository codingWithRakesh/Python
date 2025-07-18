dist = {}

for i in range(5):
    name = input("Enter a name: ")
    value = input("Enter a value: ")
    # dist[name] = value
    dist.update({name : value})

print("Dictionary:", dist)