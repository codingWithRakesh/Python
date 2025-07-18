s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Union
s3 = s1 | s2
print("Union:", s3)

# Intersection
s4 = s1 & s2
print("Intersection:", s4)
# Difference
s5 = s1 - s2
print("Difference:", s5)


#check using inbuilt methods
print("Union using union method:", s1.union(s2))
print("Intersection using intersection method:", s1.intersection(s2))
print("Difference using difference method:", s1.difference(s2))