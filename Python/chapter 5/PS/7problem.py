s = {1, 2, 3,[1, 2, 3]}  # This will raise a TypeError because lists are not hashable
# Output: TypeError: unhashable type: 'list'
# Output: TypeError: unhashable type: 'set'
# Yes, it is possible to have both int and str in a set, as shown above