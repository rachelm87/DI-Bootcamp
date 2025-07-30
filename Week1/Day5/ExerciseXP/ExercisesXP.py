#Exercise 1
#two lists 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#convert results
dictionary = dict(zip(keys, values))
print(dictionary)

#Exercise 2

#calculate cost of movie tickets for a family (Under 3 is free; 3 to 12 is $10, over 12 is $15)
#create a family dictionary and loop through through to get total costs.
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for name, age in family.items():
    if age <3:
        cost = 0
    elif 3 <= age <=12:
        cost = 10
    
    elif age > 12:
        cost = 15
    total_cost += cost
    print (f"{name}'s ticket costs ${cost}")

#print total cost
print(f"\n The family's total is: ${total_cost}")

#Exercise 3
#Create and manipulate a dictionary that contains information about the Zara brand.

brand_dict = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'U.S.': ['pink', 'green']
    }   
}
#Change the value of number_stores to 2 and show it.
brand_dict['number_stores']=2
print(f"The total number of stores is {brand_dict['number_stores']}")

#Print a sentence describing Zara’s clients using the type_of_clothes key.
clients = brand_dict["type_of_clothes"]
each_client = f"{clients[0]}, {clients[1]} and {clients[2]}"
print(f"Zara's main clients are {each_client}.")

#Add a new key country_creation with the value Spain.
brand_dict['country_creation'] = 'Spain'
print(brand_dict)

#Check if international_competitors exists and, if so, add “Desigual” to the list.
if 'international_competitors' in brand_dict:
    brand_dict['international_competitors'].append('Desigual')
    print(brand_dict)

#Delete the creation_date key
del brand_dict['creation_date']
print(brand_dict)

#Print the last item in international_competitors
print(brand_dict['international_competitors'][-1])

#Print the major colors in the US.
for color in brand_dict['major_color']['U.S.']:
    print(f'The U.S. colors are {color} and {color}')

#Print the number of keys in the dictionary.
total_keys = 0

for key, value in brand_dict.items():
    total_keys += 1 
    if isinstance(value, dict): 
        total_keys += len(value)

print("Total keys including nested:", total_keys)

#print all keys in dictionary
for key, value in brand_dict.items():
    print(key)
    if isinstance(value, dict):
        for nested_key in value:
            print(nested_key)

#Exercise 4
#You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#create dictionary mapping character to indices
user_index = {name: index for index, name in enumerate(users)}
print(user_index)

#create dictionary mapping indices to characters
index_user = {index: name for index, name in enumerate(users)}
print(index_user)

#sort it
sorted_user_dict = {name: index for index, name in enumerate(sorted(users))}
print(sorted_user_dict)
