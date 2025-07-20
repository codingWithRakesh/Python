def goodBye(name, value):
    print(f"Goodbye {name}! See you next time! Your value was {value}.")
    return "ok"


result1 = goodBye("Alice", 42)
result2 = goodBye("Bob", 100)

print(result1)
print(result2)