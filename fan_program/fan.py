class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, on=False, radius=5.00, color="Blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Getters
    def get_speed(self):
        return self.__speed

    def get_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    # Setters
    def set_speed(self, speed):
        self.__speed = speed

    def set_on(self, on):
        self.__on = on

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    #Display Output
    def display_specs(self):
        status = "ON" if self.__on else "OFF"

        print(f"Speed  : {self.__speed}")
        print(f"Radius : {self.__radius} units")
        print(f"Color  : {self.__color}")
        print(f"Status : {status}")
