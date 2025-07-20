f = open("text.txt")
print(f.read())
f.close()

# This code reads the content of "text.txt" and prints it to the console.

with open("text.txt") as f:
    print(f.read())