#Exercise 1 - Instructions: Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
#step 1 and apparently step 4 (crea)
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        return f'{self.name} is just walking around'

class Siamese(Cat):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Chartreux(Cat):
    pass

class Bengal(Cat):
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
    def __str__(self):
        return f'{self.name} is {self.age} years old, {self.weight} kilos, and a beautiful {self.color} color.'

# create a list of cat instances

bengal_obj = Bengal ("Mikey", 3, 162, "gold")
chartreux_obj = Chartreux ("Franky", 6)
siamese_obj = Siamese ("Molly", 4)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

#step 3
sara_pets= Pets (all_cats)
sara_pets.walk()
print(bengal_obj)

#Exercise - 2 Create a Dog class with methods for barking, running speed, and fighting.
#step 1
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    #add method
    def bark(self):
        return f"{self.name.capitalize()} is barking."
    #add another method
    def run_speed(self):
        return self.weight / self.age * 10
    
    #add another
    def fight(self, other_dog):
        self_winner = self.run_speed () * self.weight
        other_dog_winner = other_dog.run_speed () * other_dog.weight

        if self_winner > other_dog_winner:
            return f"{self.name} has won the fight."
        elif self_winner < other_dog_winner:
            return f"{other_dog.name} won the fight."
        else:
            return f'They tied!'

#step 2
dog1 = Dog("Fritzy", 7, 19)
dog2 = Dog("Hazel", 9, 60)
dog3 = Dog ("Romeo", 6, 50)
#test it
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


#Exercise 4 - Family and Person Classes
#step 1 define person class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18
#step 2 - family class

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members_list = []

#add methods
    def born(self, first_name, age):
        person_obj = Person(first_name, age)
        person_obj.last_name = self.last_name
        self.members_list.append(person_obj)

    def check_majority(self, first_name):
        #do they exist
        for person in self.members_list:
            if person.first_name == first_name:
                if person.is_18():
                    print ("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print ("Sorry, you are not allowed to go out with your friends.")
                return
        else:
            pass

    def family_presentation(self):
        print(f"The family's last name is: {self.last_name}.")
        print(f"The members are: .")
        for member in self.members_list:
            print(f"-- {member.first_name}:{member.age} \n")

#test
my_family = Family("Manis")
my_family.born("David", 32)
my_family.family_presentation()
my_family.born("Louise", 67)
my_family.born("Paul", 69)
my_family.born("Rachel", 37)
my_family.family_presentation()
my_family.check_majority("David")