name = "rakesh"

print("First three characters of name:", name[0:3])

print(name[-4:-1])  # Negative slicing to get characters from index -4 to -1
print(name[1:4])  # This line is incorrect and will raise a SyntaxError


print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])