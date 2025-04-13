import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


scr_width = 600
scr_height = 600
screen = Screen()
screen.setup(width=scr_width, height=scr_height)
screen.tracer(0)

turtle_racer = Player()
car_manager = CarManager()
scoreboard = ScoreBoard(scr_height / 2 - 30)

screen.listen()
screen.onkey(turtle_racer.turtle_run, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car(scr_width, scr_height)
    car_manager.driving()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle_racer) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle_racer.cross_finish():
        scoreboard.new_level()
        car_manager.increase_speed()

screen.update()
screen.exitonclick()
