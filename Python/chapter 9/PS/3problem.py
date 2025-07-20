def multipleTable(n):
    f = open(f"multiplication_{n}_table.txt", "a")
    for i in range(1, 11):
        f.write(f"{n} X {i} = {n * i}\n")
    f.close()



for i in range(2, 23):
    multipleTable(i)