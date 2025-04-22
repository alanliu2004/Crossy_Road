from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()

    def create_car(self):
        random_roll = random.randint(1, 6)
        if random_roll == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def clear(self):
        for all_car in self.all_cars:
            all_car.hideturtle()
        self.all_cars.clear()





