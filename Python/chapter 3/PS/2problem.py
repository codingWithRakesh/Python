name = input("enter your name: ")
date = input("enter the date: ")

letter = '''
    Dear <|Name|>,
    You are selected!
    Date: <|Date|>
'''
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))