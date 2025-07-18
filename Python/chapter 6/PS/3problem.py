# Avoid using 'list' as a variable name
spam_phrases = ["make a lot of money", "buy now", "subscribe this click this"]
data = input("Enter your comment: ").lower()  # Optional: lowercasing to improve matching

isCheck = True
for phrase in spam_phrases:
    if phrase in data:
        isCheck = False
        break

if isCheck:
    print("click")
else:
    print("don't click")
