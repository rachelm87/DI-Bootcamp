#OOP 


#classes and objects
#how to create a class

class Dog:
    #the constructor of a class
    def __init__(self, name, color, age, is_trained=False):
        print('the obj is being created')
        self.name = name
        self.color = color
        self.age = age
        self.is_trained = is_trained

dog1= Dog('Rex', 'brown', 10)
# print(object1.name)
print(dog1.color)
print(dog1.age)
print(dog1.__dict__)
dog1.breed = 'puddle'
dog1.name = 'Bob'
print(dog1.name)
print(dog1.breed)

#create the second object of Dog, call it dog

dog2 = Dog('Moshu', 'brown',5)

#create a new attribute to the Dog class called "is_trained" the value is boolean and the and the default is false
#then run the code again
print(dog2.is_trained)

dog3 = Dog('Fluffy','White', 7,True)
print(dog3.__dict__)
print(type(dog3))

#BEHAVIOURS = METHODS

#function > methods 
# methods = functions related to a certain class

class Dog:
    #the constructor
    #self = the object that will be created
    def __init__(self, name, color, age, is_trained=False):
        self.name = name
        self.color = color
        self.age = age
        self.is_trained = is_trained
    
    def bark(self):
        print(f'{self.name} is barking!!!')

    #create a method for the Dog class called run() if the dog's age is less than 5, print "Dog's name is running really fast"
    #if age is between 6 and 9, print ""Dog's name is running" otehrwise print "Dog's name doesn't want to run"
    #creat method called walk() that takes a parameter (meters:int) and prints "Dog's name is walking {meters}"
    def run(self):
        if self.age <= 5:
            print(f'{self.name} is running really fast!')
        elif self.age >= 6 and self.age <=9:
            print(f'{self.name} is running!')
        else:
            print(f'{self.name} does not want to run.')
    
    def walk(self, meters):
        print(f'{self.name} is walking {meters} meters.')

dog1= Dog('Rex', 'brown', 10)
dog1.bark()
dog1.run()

dog2 = Dog('Moshu', 'brown',5)
dog2.run()
dog3 = Dog('Fluffy','White', 7,True)
dog3.run()
dog3.walk(500)


        
    
