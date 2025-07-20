def removeItem(list, item):
    if item in list:
        list.remove(item)
    return list 

list = [1, 2, 3, 4, 5]
item = 3
removeItem(list, item)
print(list)