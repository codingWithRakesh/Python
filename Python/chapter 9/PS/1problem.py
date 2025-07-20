f = open("problem.txt")
data = f.read()
f.close()

if "twinkle" in data:
    print("twinkle is present")
else:
    print("twinkle is not present")