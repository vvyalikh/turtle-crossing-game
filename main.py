import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

little_turtle = Player()
car = CarManager()
scoreboard = Scoreboard()


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Little Turtle crosses the road")
screen.tracer(0)
screen.listen()
screen.onkey(little_turtle.move, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()
    scoreboard.update_level()
    for cars in car.car_list:
        if cars.distance(little_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
    if little_turtle.ycor() > 300:
        scoreboard.new_level()
        little_turtle.start_move()
        car.car_move_faster()


screen.exitonclick()
