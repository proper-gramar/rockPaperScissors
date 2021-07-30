### ROCK PAPER SCISSORS W/ OPPONENT ###
from random import *

rps = 0
while rps != 4:
    rps = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors, 4 to quit: "))
    compChoice = randint(1, 3)

    def rpsChoice(num):
        switcher = {
            1: "Rock",
            2: "Paper",
            3: "Scissors"
        }
        return switcher.get(num, "error")


    print("You chose " + str(rpsChoice(rps)) + ", Opponent chose " + str(rpsChoice(compChoice)))
    if rps == compChoice:
        print("Draw, you got lucky")
        continue

    if rps == 1 and compChoice == 3:
        print("You win!")
        continue
    if rps == 2 and compChoice == 1:
        print("You win!")
        continue
    if rps == 3 and compChoice == 2:
        print("You win!")
        continue
    else:
        print("Opponent whooped your ass")

    continue
