from datetime import datetime
from datetime import date

class Person:

    id_number = 1

    def __init__(self, name, last_name, birth_date):
        self.name = name
        self.last_name = last_name
        self.birth_date = self.parse_birthdate(birth_date)
        Person.id_number += 1

    @staticmethod
    def parse_birthdate(date_str):
        return datetime.strptime(date_str, '%d-%m-%Y').date()
    
    @staticmethod
    def format_name(name):
        if not name[0].isupper():
            return name.capitalize()
        else:
            return name
        
    @classmethod
    def from_age(cls, name, last_name, age):
        current_year = datetime.today().year
        birth_year=current_year - age
        birth_date = f'1-1-{birth_year}'
        return cls(name,last_name,birth_date) #the 1-1 means January 1
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    
    def __str__(self): #gives info inside info
       return f'name: {self.name} \n last name: {self.last_name} \n age: {self.age}'
    
    def __repr__(self): #gives information on front end to the developer
        return f'{self.__dict__}'
    
    #dunder methods allow us to compare

    def __lt__(self,other):
        return self.age < other.age # less than
    

p1 = Person('jon', 'snow', '21-08-1990')
print(type(p1.birth_date))
print(p1.name)
print(p1)
print(repr(p1))
p2 = Person.from_age('Arya', 'Stark', 18)
p3 = Person.from_age('Arya', 'Stark', 18)
print(p2.birth_date)
print(p1.age)

print(Person.format_name('lise')) #we want different ways of creating the object
print(p1 > p2)
