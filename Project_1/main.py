"""
1 for snake
-1 for water
0 for gun
"""
import random

choices = [1, -1, 0]
computer = random.choice(choices)

youstr= input("Enter your choice(s/w/g): ")
yourdict={
    "s": 1,
    "w": -1,
    "g": 0
}

yourdict2={
     1:"Snake",
    -1: "Water",
    0: "Water"
}
you= yourdict[youstr]

print(f"You choose {yourdict2[you]} \nComputer choose {yourdict2[computer]}")

if computer== you:
    print("it's a draw")
else:
    if computer==1 and you==0:
        print("You win")
    elif computer==1 and you==-1:
        print("You lose")

    elif computer==-1 and you==0:
        print("You lose")
    elif computer==-1 and you==1:
        print("You win")

    elif computer==0 and you==1:
        print("You lose")
    elif computer==0 and you==-1:
        print("You win")