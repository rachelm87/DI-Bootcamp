#Exercise1: Cats
#create CAT class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat ('Pharoah', 6)
cat2 = Cat ('Fluffy', 8)
cat3 = Cat ('Onyx', 3)

#create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    print(f'The oldest cat is {oldest.name}, and is {oldest.age}')

find_oldest_cat(cat1, cat2, cat3)

#Exercise2 - Dog Class with barking/jumping
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def barking (self):
        print(f'{self.name} goes woof!')
    
    def jumping (self): 
        print(f' {self.name} jumps {self.height * 2} cm high!')

    def dog_details (self):
        print(f'The dog is named {self.name} and they are {self.height} cm tall.')

#create dog objects
davids_dog = Dog('Fritz', 50)
sarahs_dog = Dog('Einstein', 40)

#print dog details and call methods
print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
sarahs_dog.barking()
sarahs_dog.jumping()
davids_dog.barking()
davids_dog.jumping()

#compare sizes Step 4
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller!")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller!")
else:
    print("Both dogs are the same height!")

#Exercise 3 - Who is the song producer?
#create song class and attribute
class Song:
    def __init__(self, song, lyrics):
        self.song = song
        self.lyrics = lyrics

#add a method
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

lyrics_list = ["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]
stairway = Song("Stairway to Heaven", lyrics_list)
#call it
stairway.sing_me_a_song()

#Exercise 4 - Afternoon at the Zoo
#Create a Zoo class to manage animals. The class should allow adding animals
# displaying them, selling them, and organizing them into alphabetical groups.
#Step 1 - define the zoo class
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    ##adding a method
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            pass
    
    def get_animals(self):
        print(f'The animals are {self.animals}.')
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            pass
    
    def sort_animals(self):
        self.animals.sort()
        groups = {}

        for animal in self.animals:
            letter = animal[0]
            if letter not in groups:
                groups[letter] = [animal]
            else:
                groups[letter].append(animal)

        self.animal_groups = groups
    
    def get_groups(self):
        for letter, animal in self.animal_groups.items():
            print(f"{letter}: {animal}")

#create a zoo object
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
    
