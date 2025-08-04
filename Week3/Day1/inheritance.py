#inheritance: Parent and Child class

class Parent:
    def speak(self):
        print(f'Parent speaking')

class Child(Parent):
    def speak(self):
        print(f'Child speaking')

class Grandchild(Child):
    pass

# obj1 = Child()
# obj1.speak()

# obj2 = Grandchild()
# obj2.speak()


class Animal:

    def __init__(self, name, family,legs):
        self.name = name
        self.family = family
        self.legs = legs

    def sleep(self):
        return f'{self.name} is sleeping - from Animal'

class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age

    def bark(self):
        return f'{self.name} is barking'
    
class Cat(Animal):
    def __init__(self, name, family, legs, friendly, age, nickname):
        super().__init__(name, family, legs)
        self.friendly = friendly
        self.age = age
        self.nickname = nickname
    
    def get_crazy(self):
        if self.friendly:
            return f'{self.name} doesn\'t get crazy'
        else:
            return f'{self.name} is running in full power'


class Alien:
    def __init__(self, name, planet):
        self.personal_name = name
        self.planet = planet

    def bark(self):
        return f'{self.name} goes Ululululu'

class AlienDog(Alien, Dog):
    def __init__(self, name, family, legs, trained, age, planet):
        Alien.__init__(self, name, planet)
        Dog.__init__(self, name, family, legs, trained, age)


dog1 = Dog('Rex', 'Canine', 4, True, 5)
print(dog1.bark())
print(dog1.sleep())

alien_dog1 = AlienDog('Buba', 'Canine', 6, True, 135, 'Jupyter')
print(alien_dog1.bark())

print(Dog.bark(alien_dog1)) #specifying from which class I want the method to be called

# create a AlienCat class that inherit from Cat and Alien.
# create a method fly_away that calls the method get_crazy(), prints it output and add 'as an alien cat'
# 
class AlienCat(Cat, Alien):
    def __init__(self, name, family, legs, friendly, age, nickname, planet):
        Cat.__init__(self, name, family, legs, friendly, age, nickname)
        Alien.__init__(self, name, planet)
        
    def fly_away(self):
        output = f'{self.get_crazy()} as an alien cat'
        return output

aliencat1 = AlienCat('Flufy', 'Feline', 6, False, 200, 'fluflu','jupyter')
print(aliencat1.fly_away())

