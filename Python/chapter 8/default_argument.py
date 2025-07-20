def goodBye(name, ending="Thank you!"):
    print(f"Goodbye {name}! {ending}")
    return "ok"


result1 = goodBye("Alice", "See you soon!")
result2 = goodBye("Bob")

print(result1)
print(result2)