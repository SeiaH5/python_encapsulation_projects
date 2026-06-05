from car import Car
import time 

try:
    print("=====CAR=====")
    
    year = int(input("Enter year model: "))
    make = input("Enter Make/Brand: ")

    car = Car(year, make)
    
    print(f"Current Speed: {car.get_speed()}\n")

    for i in range(5):
        car.accelerate()
        print("\033[2m\033[3mAccelerating\033[0m")
        print(f"Current Speed: {car.get_speed()}")
        time.sleep(1)

    print()

    for i in range(5):
        car.brake()
        print("\033[2m\033[3mBraking\033[0m")
        print(f"Current Speed: {car.get_speed()}")
        time.sleep(1)

except Exception as e:
    print(f"\n\033[31mError: {e}\033[0m\n")
