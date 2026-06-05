from datetime import datetime

class Car:
    def __init__(self, year_model, make):
        current_year = datetime.now().year

        if 1886 <= year_model <= current_year:
            self.__year_model = year_model
        else:
            raise ValueError("\n\033[31m\nInput a valid year model.\033[0m\n")

        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
