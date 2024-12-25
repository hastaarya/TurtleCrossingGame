from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle() #hide the arrow at the start of the game
        self.penup() #hide the line 
        self.goto(-260,260) #set coordinate to top-center

    def update_scoreboard(self): #writing texts to the screen
        self.clear()
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self): #increase score and update the screen by clearing the screen and writing a new one
        self.level+=1
        self.update_scoreboard()

    def game_over(self): #print out game over texts
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align="center", font=FONT)