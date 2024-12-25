from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):        
        self.move_speed = 0.1        
        self.all_car = []
        self.create_car()        
 
    def create_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-270,280))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)  
            self.all_car.append(new_car)        
        self.move_car()

    def move_car(self):
        for car in self.all_car:            
            car.forward(MOVE_INCREMENT)

    def next_level(self):
        self.move_speed*=0.7

