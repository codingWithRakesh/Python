friends = ["Rakesh", "Nitish", "Aftar", True, 1, 2.5 , None]

print("Friends list:", friends)
friends.append("New Friend")
print("Updated Friends list:", friends)

l1 = [52,7, 9, 10, 11, 12, 13, 14, 15]

l1.sort()
print("Sorted list:", l1)

l1.reverse()
print("Reversed list:", l1)

l1.insert(2, 100)
print("List after inserting 100 at index 2:", l1)

value = l1.pop(3)
print("Value popped from index 3:", value)

print(value, "is removed from the list")
print("Final list:", l1)