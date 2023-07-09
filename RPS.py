import random

# Player Class
class Player():

    # Initialize class variables
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.throw = ''

    # Method to keep track of player score
    def setScore(self, value):
        self.score = self.score + value

    # Method to pull the player score
    def getScore(self):
        return self.score

    # Method to accept input of Rock, Paper, or Scissor
    def setThrow(self):
        self.throw = input("Enter 'Rock', 'Paper' or 'Scissors': ").lower()

# Computer Opponent Class
class Comp_Opponent():
    
    # Initialize class variables
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.throw = ''

    # Method to keep track of the computer score
    def setCompScore(self, value):
        self.score = self.score + value

    # Method to pull the computer score
    def getCompScore(self):
        return self.score

    # Method to randomly choose Rock, Paper, or Scissor for the computer
    def setCompThrow(self):
        self.throw = random.choice(['Rock', 'Paper', 'Scissors']).lower()

# Game Class
class game():

    # Initialize variables of the game class
    def __init__(self):
        self.player_1 = Player("You")
        self.player_2 = Comp_Opponent("SkyNet")
        self.rounds = 0

    # Method for determining victory in the game
    def checkVictory(self):
        print(f'\nYou have thrown {self.player_1.throw.title()}, and the Computer has thrown {self.player_2.throw.title()}')
        
        # Win conditions and outputs
        if self.player_1.throw == self.player_2.throw:
            print("\nBoo, it's a draw, not cool!")
        elif (self.player_1.throw == 'rock' and self.player_2.throw == 'scissors') or (self.player_1.throw == 'scissors' and self.player_2.throw == 'paper') or (self.player_1.throw == 'paper' and self.player_2.throw == 'rock'):
            print(f'\n{self.player_1.name} have bested the computer this round!')
            self.player_1.setScore(1)
        else:
            print(f'\n{self.player_2.name} has beat you this round!')
            self.player_2.setCompScore(1)
    
    # Round + 1
    def setRounds(self, value):
        self.rounds += value

    # Determines who won after multiple games/rounds
    def whoWon(self):
        print(f"{self.player_1.name} won {self.player_1.getScore()} rounds. \n{self.player_2.name} won {self.player_2.getCompScore()} rounds")
        print(f"\nAnd the winner is....")

        if self.player_1.score == self.player_2.score:
            print("Game is a draw....Lame.")
        elif self.player_1.score > self.player_2.score:
            print("You!  Congratulations!")
        else:
            print("The computer :(.  Better luck next time!")

    # Driver for the game, calls above methods
    def gameOn(self):
        gaming = True # Boolean to keep loop going.  Set to false when player wants to quit
        while gaming:
            self.player_1.setThrow() # Player input of Rock, Paper, or Scissor
            self.player_2.setCompThrow() # Computer random choice of Rock, Paper or Scissor
            self.checkVictory() # Calls the method to see who won this round

            # Tells the player how many games/rounds they have won in this session.
            print(f'\n{self.player_1.name} have won {self.player_1.getScore()} rounds, and {self.player_2.name} has won {self.player_2.getCompScore()} rounds')
            
            # Asks player if they want to keep playing or quit.
            endGame = input(f"\n{self.player_1.name} have played {self.rounds} rounds.  Would you like to keep playing? (Y/N) ").lower()
            
            # Conditionals to continue or end the game
            if endGame == 'y':
                self.setRounds(1) # Increase round by 1
                continue
            elif endGame == 'n':
                gaming = False
                self.whoWon() # Calls the method to end the game and tell the player who won the most games/rounds
            else:
                endGame = input("Please input 'Y' to keep playing or 'N' to quit.").lower()
            

rps = game()
rps.gameOn()