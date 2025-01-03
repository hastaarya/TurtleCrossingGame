from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape = "turtle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.penup()
        self.reset_position()        

    def reset_position(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):                
        self.forward(MOVE_DISTANCE)
    
    def move_down(self):                
        self.backward(MOVE_DISTANCE)
    
