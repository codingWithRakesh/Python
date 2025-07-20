# Open and read the file with utf-8 encoding
with open("dunky.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Check and replace 'donkey' in a case-insensitive way
if "donkey" in content.lower():
    # Replace only exact lowercase "donkey"
    content = content.replace("donkey", "XXXXXX")

    # Write the updated content back to the file
    with open("dunky.txt", "w", encoding="utf-8") as f:
        f.write(content)

    print("donkey is present")
else:
    print("donkey is not present")
