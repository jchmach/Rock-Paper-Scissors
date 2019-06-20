"""Author: Justin Mach
   Purpose: To practice OOP and GUI development in Python 
"""
import random
from tkinter import * 


class myGame:
    """
    Represents the 'game master'. Controls and manipulates gameplay, player and computer scores
    and updates the users moves.
    Fields:
        playerScore - represents the score of the player in the game
        cpuScore - represents the score of the computer in the game
        playerMove - represents the choice that the user makes. Initialized to -1 to represent no move chosen
    """
    def __init__(self):
        self.playerScore = 0
        self.cpuScore = 0
        self.playerMove = -1
    
    def getWinner(self):
        """
        Calculates the computer's move and prints their choice and returns who wins 
            Winning is based off of numbers:
                0 - represents rock chosen
                1 - represents paper chosen
                2 - represents scissors chosen
            By comparing these numbers, calculating victor for each round is simple
        Return: 
            -1 - if a tie occurs
            0 - if the computer wins
            1 - if the player wins 
        """
        cpuMove = random.randint(0,2)
        self.drawComp(cpuMove)
        if (self.playerMove == cpuMove):
            return -1
        elif (self.playerMove == 0 and cpuMove == 2):
            self.playerScore += 1
        elif (self.playerMove == 1 and cpuMove == 0):
            self.playerScore += 1
        elif (self.playerMove == 2 and cpuMove == 1):
            self.playerScore += 1
        else:
            self.cpuScore += 1
            return 0
        return 1

    def drawComp(self, move):
        """
        Updates the choice computer made by displaying it's move on the canvas
        Fields: 
            move - represents what the computer has chosen as their move. This dictates what is printed onscreen
        """
        if (move == 0):
            gameCanvas.create_image(800, 30, image = rockPhoto, anchor = NE)
        elif (move == 1):
            gameCanvas.create_image(800, 30, image = paperPhoto, anchor = NE)
        else:
            gameCanvas.create_image(800, 30, image = scissorsPhoto, anchor = NE)


def playRock():
    """
    Updates the player move to rock, prints their move and update the game info (score, outcome)
    if the rock button is pressed
    """
    newGame.playerMove = 0
    gameCanvas.delete("all")
    gameCanvas.create_image(50, 30, image = rockPhoto, anchor = NW)
    result = newGame.getWinner ()
    if result == -1:
        outcome.set ("Tie!")
    elif result == 0:
        cpuScore.set(str(newGame.cpuScore))
        outcome.set ("You lose! Computer Wins.")
    else:
        playerScore.set(str(newGame.playerScore))
        outcome.set("You Win!")

def playPaper():
    """
    Updates the player move to paper, prints their move and update the game info (score, outcome)\
    if the paper button is pressed
    """
    newGame.playerMove = 1
    gameCanvas.delete("all")
    gameCanvas.create_image(50, 30, image = paperPhoto, anchor = NW)
    result = newGame.getWinner ()
    if result == -1:
        outcome.set ("Tie!")
    elif result == 0:
        cpuScore.set(str(newGame.cpuScore))
        outcome.set ("You lose! Computer Wins.")
    else:
        playerScore.set(str(newGame.playerScore))
        outcome.set("You Win!")

def playScissors():
    """
    Updates the player move to scissors, prints their move and update the game info (score, outcome)
    if the scissors button is pressed
    """
    newGame.playerMove = 2
    gameCanvas.delete("all")
    gameCanvas.create_image(50, 30, image = scissorsPhoto, anchor = NW)
    result = newGame.getWinner ()
    if result == -1:
        outcome.set ("Tie!")
    elif result == 0:
        cpuScore.set(str(newGame.cpuScore))
        outcome.set ("You lose! Computer Wins.")
    else:
        playerScore.set(str(newGame.playerScore))
        outcome.set("You Win!")

def resetGame():
    """
    Resets the scores, moves, and outcomes if the reset button is pressed
    """
    newGame.playerScore = 0
    newGame.cpuScore = 0
    playerScore.set("0")
    cpuScore.set("0")
    outcome.set("")
    gameCanvas.delete("all")

#=====Main======
gameWindow = Tk()
#gameWindow.maxsize(width = 850, height = 650)
gameWindow.minsize(width = 850, height = 650)    
gameWindow.title ("Rock Paper Scissors")
gameWindow.config(bg = "#10140f")
playerScore = StringVar ()
cpuScore = StringVar ()
outcome = StringVar ()
newGame = myGame()
playerScore.set("0")
cpuScore.set("0")
rockPhoto = PhotoImage(file='Rock V3.png')
paperPhoto = PhotoImage(file='Paper V2.png')
scissorsPhoto = PhotoImage(file='Scissors V2.png')
player = Label (gameWindow, text = "Player", font = ("Arial", "30", "bold"), bg = "#10140f", fg = "#35de00")
computer = Label (gameWindow, text = "Computer", font = ("Arial", "30", "bold"), bg = "#10140f", fg = "#35de00")
playerScorelbl = Label (gameWindow, textvariable = playerScore, font = ("Arial", "30", "bold"), bg = "#10140f", fg = "#35de00")
compScorelbl = Label (gameWindow, textvariable = cpuScore, font = ("Arial", "30", "bold"), bg = "#10140f", fg = "#35de00")
outcomelbl = Label (gameWindow, textvariable = outcome, font = ("Arial", "20", "bold"), bg = "#10140f", fg = "#35de00")
gameCanvas = Canvas (gameWindow, borderwidth = 0, highlightthickness = 0, bg = "#10140f", width = 850)
playerChoices = LabelFrame (gameWindow, text = "Choose your shape", bg = "#10140f", fg = "#35de00")
reset = Button (gameWindow, text = "Reset", font = ("Arial", "20", "bold"), width = 30, height = 1, command = lambda: resetGame())
paper = Button (playerChoices, image=paperPhoto, bg = "#10140f", command = lambda: playPaper())
scissors = Button (playerChoices, image=scissorsPhoto,  bg = "#10140f", command = lambda: playScissors())
rock = Button (playerChoices, image=rockPhoto, bg = "#10140f", command = lambda: playRock())
#===========================
player.place (anchor = "center", x = 75, y = 32)
computer.place (anchor = "center", x = 735, y = 32)
playerScorelbl.place (anchor = "center", x = 400, y = 32)
compScorelbl.place (anchor = "center", x = 450, y = 32)
gameCanvas.place (anchor = "center", x = 425, y = 200)
outcomelbl.place (anchor = "center", x = 425, y = 360)
playerChoices.place (anchor = "center", x = 425, y = 475)
paper.grid (row = 0, column = 1, padx = 10, pady = 5)
rock.grid (row = 0, column = 0, padx = 10, pady = 5)
scissors.grid (row = 0, column = 2, padx = 10, pady = 5)
reset.place (anchor = "center", x = 425, y = 600)
gameWindow.mainloop()
