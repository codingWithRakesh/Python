marks = []

for i in range(3) :
    num = int(input("enter your marks"))
    marks.append(num)

total = 0

for i in range(len(marks)):
    total += marks[i]

persentage = (total / 300) * 100

passSubject = False

for i in range(len(marks)):
    if marks[i] > 33 :
        passSubject = True
    else :
        passSubject = False
        break

passOverall = persentage >= 40

if(passOverall and passSubject):
    print("you pass the exam")
else :
    print("fail your exam")