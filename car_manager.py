from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_y = random.randint(-220, 220)
            new_car.goto(300, new_y)
            self.car_list.append(new_car)

    def car_move(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def car_move_faster(self):
        self.car_speed += MOVE_INCREMENT


