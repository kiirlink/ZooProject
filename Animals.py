# ==========================================================
# ZooProject
#
# A simple console application written in Python using
# object-oriented programming (OOP).
#
# Features:
# - Create new animals
# - Display the list of animals
# - Feed animals
# - Play with animals
# - Let animals sleep
# - View animal information
#
# Each animal has:
# - Name
# - Species
# - Age
# - Satiety level (0–100%)
#
# The project demonstrates:
# - Classes and objects
# - Constructors (__init__)
# - Instance and class attributes
# - Static methods
# - Lists
# - Loops
# - Exception handling
# - Match-case statements
#
# Author: Pavel Kodochigov
# Language: Python 3
# ==========================================================

class Animal:
    all_instances = []
    def __init__(self, name, species, age, eaten):
        self.name = name
        self.species = species
        self.age = age
        self.eaten = eaten
        
        Animal.all_instances.append(self)  # Add the object to the shared list
    
    def __str__(self):
        return f"{self.name} - {self.species}, {self.age} years old, fed {self.eaten}%"
    
     
    def info(self):
        print(self)
        
    def feed(self):
        if (self.eaten + 20) > 100 :
            self.eaten = 100
            print(f'{self.name} is already full')
        else :
            self.eaten += 20
            print(f'{self.name} is eating.')
    
    def play(self):
        if (self.eaten - 15) < 0 :
            self.eaten = 0
            print(f'{self.name} is very hungry and doesn\'t want to play.')
        else :
            self.eaten -= 15
            print(f'{self.name} is playing.')
    
    def sleep(self):
        if (self.eaten + 10) > 100 :
            self.eaten = 100
        else :
            self.eaten += 10
        print(f'{self.name} is sleeping...')
    
    @staticmethod
    def create_from_input():
        try:
            name = input("Name: ")
            species = input("Species: ")
            age = int(input("Age: "))
            if age < 0:
                print("Age cannot be negative.")
                return
            eaten = int(input("Satiety: "))
            eaten = max(0, min(100, eaten)) # range from 0 to 100
            Animal(name, species, age, eaten)
        except ValueError:
            print("Age and satiety must be numbers.")
            

animal1 = Animal("Barsik", "cat", 3, 50)
animal2 = Animal("Bobik", "dog", 5, 20)

def show_animals():
    print('\n===== Animals =====')
    i = 0
    for animal in Animal.all_instances :
        print(i, animal.name)
        i += 1

while True:
    print('\n===== Zoo =====\n1. Add an animal\n2. Choose an animal\n3. Show all animals\n0. Exit')
    
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    match choice:
        case 1:
            Animal.create_from_input()
            continue
        case 2 :
            show_animals()
            
            try:
                animal_number = int(input("Choose an animal number: "))
            except ValueError:
                print("Please enter a number")
                continue        
    
            try:
                animal = Animal.all_instances[animal_number]

                todo = int(input("1. Feed, 2. Play, 3. Sleep, 4. Show information: "))
                
                match todo:
                    case 1:
                        animal.feed()
                    case 2:
                        animal.play()
                    case 3:
                        animal.sleep()
                    case 4:
                        animal.info()
                    case _:
                        print("Unknown command")
            except IndexError:
                print("There is no such animal in our zoo")
            except ValueError:
                print("Please enter a number")
        case 3:
            show_animals()
        case 0:
            break
        case _:
            print("No such menu option")
 
