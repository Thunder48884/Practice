'''
Make a class that will function as a game handler. 
The game you will make is rock paper scissors. 
The instructions will be vague in order to let you be more 
creative with the solution. You must at least one class, 
and all of your code to run the game must be in that class. 
It is recommended you make a few functions to complete this. 
The user should be able to pick their choice and the program 
will tell them if the user won, the computer won or there was 
a tie. 
'''
import os

class gameHandler():
    def start(p1, p2):
        x = gameHandler(p1, p2)
        x.RPS()
        return x
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.leaderboard = {}
        self.leaderboard[self.p1] = 0
        self.leaderboard[self.p2] = 0

    def clearInput(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def takeInput(self, p):
        print(f"{p}'s turn...")
        x = ''
        while(not(x == 'r' or x == 'p' or x == 's')):
            x = input("Choose Rock{r}, Paper{p}, Scissors{s}: ")

        return x
    
    def turn(self):
        one = self.takeInput(self.p1)
        self.clearInput()
        two = self.takeInput(self.p2)
        self.clearInput()
        input("Both players ready?")
        winner = self.decide(one, two)
        if winner == 0:
            input(f"Both players have chosen the same thing!\nIt's a tie!")
        elif winner == 1:
            input(f"{self.p1}, wins!")
            self.leaderboard[self.p1] += 1
            self.clearInput()
        else:
            input(f"{self.p2}, wins!")
            self.leaderboard[self.p2] += 1
            self.clearInput()



    def decide(self, one, two):
        if (one == two):
            return 0
        elif(one == 'r' and two == 's'):
            return 1
        elif(one == 's' and two == 'p'):
            return 1
        elif(one == 'p' and two == 'r'):
            return 1
        else:
            return 2
    
    def RPS(self):
        print("Welcome to Rock, Paper, Scissors!")
        print("You will be playing 2 out of 3.\n")
        print("You will take turns putting in your choice.\nThe other player should look away while you pick.")
        x = input("Confirm?")
        self.clearInput()
        while (self.leaderboard[self.p1] != 2 and self.leaderboard[self.p2] != 2):
            self.turn()

        if (self.leaderboard[self.p1] == 2):
            print(f"{self.p1}, has won overall!!!\nCONGRATS!!!\n")
        else: 
            print(f"{self.p2}, has won overall!!!\nCONGRATS!!!\n")
        
        print("Game Over!!!\nPlease play again!")

        
game = gameHandler.start("Player 1", "Player 2")