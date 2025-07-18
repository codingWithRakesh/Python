s = set()

s.add(20)
s.add(20.0)
s.add("20")

print("Set:", s)
# Output: Set: {20, '20'}
print(len(s))  # Output: 2, since 20 and '20' are considered different types
# Yes, it is possible to have both int and str in a set, as shown above