# Week 10 assignment 1
# Number Guessing game
# Date last modified: March 11, 2024
# Last modified by: Isaak Grettum
# ===============================
import random

def makeAGuess(string, y):
    x = input(string)
    try:
        x = int(x)
    except:
        print("That wasn't even a number, or atleast not a very good one.")
        return True

    if(int(x) == y):
        print("You guessed correctly, Congrats!")
        return False
    if (x<y):
        print(f"cough, higher, cough...")
        return True
    if (x>y):
        print(f"cough, lower, cough...")
        return True
    
y = random.random() * 100
y = int(y)

while(makeAGuess("Make a guess between 1-100: ",y)):
    print("That was incorrect please try again.\n")



