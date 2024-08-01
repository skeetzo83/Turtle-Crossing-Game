import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
car_manager = CarManager()
car_manager.create_car()
screen.onkey(key="Up", fun=player.move_up)
game_is_on = True
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for number in range(0, len(car_manager.all_cars)):
        if player.distance(car_manager.all_cars[number]) < 30:
            car_manager.starting_move_distance = 0
            scoreboard.game_over()
            game_is_on=False
    if player.ycor() > 300:
        scoreboard.add_score()
        player.okay()
        car_manager.passed()

screen.exitonclick()