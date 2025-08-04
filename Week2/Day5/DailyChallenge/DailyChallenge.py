#Daily Challenge - Old McDonalds Farm
# You are given example code and output. 
# Your task is to create a Farm class that produces the same output. 

#STEPS 1 -2  - CREATE TEH CLASS
class Farm:
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals = {}
    #step 3 - implement add_animal method
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    #step 4 - implement get_info method
    def get_info(self):
        print(f"Old {self.name} had a farm, and on his farm, he had:")
        for animal_type, count in self.animals.items():
            print(f"{count} {animal_type}(s)")
        print("E-I-E-I-O")
    
    #Bonus - Expand the farm: Step 6: Implement the get_animal_types
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    #Step 7: Implement the get_short_info Method
    def get_short_info(self):
        animals = self.get_animal_types()
        animal_names = []

        for animal in animals: 
            if self.animals[animal]>1:
                animal_names.append(animal + "s")
            else: animal_names.append(animal)

        if len(animal_names) > 1:
            first_animal = ", ".join(animal_names[:-1]) + ' and ' + animal_names[-1]
        else:
            first_animal = animal_names[0]

        return(f"{self.name.capitalize()}'s farm has {first_animal}.")




# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow')
macdonald.add_animal('pig')
macdonald.add_animal('horse')
macdonald.add_animal('pig')
macdonald.add_animal('horse')
macdonald.add_animal('pig')
print(macdonald.get_info())
print(macdonald.animals)
print(macdonald.get_animal_types())
print(macdonald.get_short_info())