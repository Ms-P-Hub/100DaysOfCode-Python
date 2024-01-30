from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1 :
            car = Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(COLORS))
            y_position = random.randint(-250,250)
            car.goto(300,y_position)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)