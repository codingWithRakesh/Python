marks = {
    "Rakesh" : 9.45,
    "Nitish" : 8.80,
    "After" : 7.65,
}

print(marks.items())  # Print all key-value pairs in the dictionary
print(marks.keys())   # Print all keys in the dictionary
print(marks.values()) # Print all values in the dictionary
marks.update({"Rakesh": 9.50,"John": 8.90})  # Update Rakesh's marks
print(marks)

print(marks.get("Rakesh"))  # Get Rakesh's marks using get method
print(marks["Rakesh"])  # Get Rakesh's marks using direct access