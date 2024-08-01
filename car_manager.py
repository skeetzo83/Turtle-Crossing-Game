from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-250, 260)
            new_car.goto(280, y_pos)
            self.all_cars.append((new_car))


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.starting_move_distance)

    def passed(self):
        self.starting_move_distance += 10

    def car_clear(self):
        self.all_cars