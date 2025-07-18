friends = ["Rakesh", "Nitish", "Aftar", True, 1, 2.5 , None]

print("Friends list:", friends)
print("First friend:", friends[0])

friends[1] = "Aftab"
print("Updated second friend:", friends[1])

print(friends[1])

print("Friends list length:", len(friends))
print(friends[0:3])  # Slicing to get first three friends
print(friends[-3:-1])  # Negative slicing to get friends from index -3 to -1
print(friends[1:4])  # Slicing to get friends from index 1 to 3