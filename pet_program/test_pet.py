from pet import Pet

print("\033[32m===== PET'S INFORMATION FORM =====\033[0m")

count_pets = int(input("Enter number of pets\033[2m\033[3m(Example: 2)\033[0m: "))

pets = []

for i in range(count_pets):
    my_pet = Pet()
    
    print(f"\n\033[1mPet #{i+1} Information\033[0m")
    pet_name = input("Enter your pet's name\033[2m\033[3m(Example: Jinggoy)\033[0m: ")
    animal_type = input("Enter your pet's animal type\033[2m\033[3m(e.g. Dog, Cat, Bird)\033[0m: ")
    pet_age = int(input("Enter your pet's age in months\033[2m\033[3m(Example: 10)\033[0m: "))

    my_pet.set_name(pet_name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(pet_age)

    pets.append(my_pet)

print("\n"*3, "\033[1m===== YOUR PETS' INFORMATION =====\033[0m")
for pet in pets:
    print(f"\033[1m\033[34m{pet.get_name()}\033[0m")
    print("Animal Type:", pet.get_animal_type())
    print(f"Age: {pet.get_age()} months")
    print("-"*20)