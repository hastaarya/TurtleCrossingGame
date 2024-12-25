import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()
    score.update_scoreboard()
    #turtle finish line, next level            
    car.create_car()
    if player.ycor() > 270:
        score.increase_score()        
        car.next_level()
        player.reset_position()

    #turtle collides with car
    for cars in car.all_car:
        if player.distance(cars) < 15:
            game_is_on = False
            score.game_over()

screen.exitonclick()
