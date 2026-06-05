from pet import Pet

pet1 = Pet()

print("\033[32m===== PET'S INFORMATION FORM =====\033[0m")

pet_name = input("Enter your pet's name: ")
animal_type = input("Enter your pet's animal type\033[2m(e.g. Dog, Cat, Bird)\033[0m: ")
pet_age = input("Enter your pet's age: ")


pet1.set_name(pet_name)
pet1.set_animal_type(animal_type)
pet1.set_age(pet_age)

print("\n\033[1m===== YOUR PET'S INFORMATION =====\033[0m")
print("Name:", pet1.get_name())
print("Type:", pet1.get_animal_type())
print("Age:", pet1.get_age())