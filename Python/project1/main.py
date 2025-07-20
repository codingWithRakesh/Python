import random

'''
1 for snake
-1 for water 
0 for gun
'''

computer = random.choice([1, -1, 0])
yourStr = input("Enter your choice (S/W/G): ")
yourDict = {"S": 1, "W": -1, "G": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = yourDict[yourStr.upper()]

print(f"You chose: {reversedDict[you]}")
print(f"Computer chose: {reversedDict[computer]}")

if you == computer:
    print("It's a tie!")

else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Invalid input, please try again.")
    