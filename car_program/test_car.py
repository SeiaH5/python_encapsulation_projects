from car import Car

try:
    year = int(input("Enter year model: "))
    make = input("Enter Brand: ")

    car = Car(year, make)
    
    print("\nStarting")

    print("Current Speed:", car.get_speed())


except:
    print("\033[31mError\033[0m")