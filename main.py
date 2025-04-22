import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
START_SPEED = 0.1
current_speed = START_SPEED
cars = CarManager()

screen.onkey(player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(current_speed)
    screen.update()

    #Create new cars and moves them
    cars.create_car()
    cars.move_car()

    #Detects if player reaches the finish line
    if player.ycor() >= 280:
        player.reset()
        cars.clear()
        scoreboard.increase_level()
        current_speed *= 0.5

    #Detects if player collides with cars
    for car in cars.all_cars:
        if player.distance(car) <= 25 and car.ycor() - 20 < player.ycor() < car.ycor() + 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()