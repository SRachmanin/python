# -*- coding: cp1251 -*-

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"The {self.name} run."

    def stop(self):
        return f"\nThe {self.name} has stopped."

    def turn(self, direction):
        return f"\nThe {self.name} turned {direction}."

    def show_speed(self):
        return f"\nYour speed is {self.speed}."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"\nYour speed is high - {self.speed}!"
        else:
            return f"Speed of {self.name} is normal"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"\nYour speed is high - {self.speed}!"
        else:
            return f"Speed of {self.name} is normal"


class PoliceCar(Car):
    pass


town = TownCar("Mazda", 95, "gray", False)
print("1. " + town.go(), town.show_speed(), town.turn("left"), town.turn("right"), town.stop())

sport = SportCar("Ferarri", 220, "green", False)
print("2. " + sport.go(), sport.show_speed(), sport.turn("left"), sport.stop())

work = WorkCar("WAZ", 40, "black", False)
print("3. " + work.go(), work.show_speed(), work.turn("right"), work.stop())

police = PoliceCar("Lada", 90, "white", True)
print("4. " + work.go(), work.show_speed(), work.turn("right"), work.stop())
