marks = []

for i in range(5):
    mark = int(input("enter a mark: "))
    marks.append(mark)

print("List of marks:", marks)

sorted_marks = marks.sort()
print("Sorted marks:", marks)