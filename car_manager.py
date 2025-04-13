from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_CHANCE = 0.2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_chance = CAR_CHANCE

    def create_car(self, scr_width, scr_height):
        if random.random() < self.car_chance:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(scr_width / 2 + 20, random.randint(-scr_height / 2 + 50, scr_height / 2 - 50))
            self.all_cars.append(new_car)

    def driving(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 1.4
        self.car_chance += 0.06
