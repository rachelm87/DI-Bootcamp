#exercise 1: what are you learning?
def display_message():
    '''prints a sentence about how i'm learning about functions'''
    print("I am learning about functions in Python.")
display_message()

#exercise 2: what's your favorite book?
'''this function gets the user's favorite book and states it to them.'''
def favorite_book():
    return input("What is your favorite book?: ")
book = favorite_book()
print(f'Your favorite book is: {book}!')

#exercise 3: 
def describe_city(city, country="Unknown"):
    '''takes the city and says which country its in'''
    return f'{city} is in {country}'
print(describe_city("Paris", "France"))
print(describe_city("Reykjavik", "Iceland"))
print(describe_city("Paris"))

#exercise 4: Random
import random
'''creates a function that generates random numbers and compares them'''
def random_numero():
    try:
        your_number = int(input("Enter a number from 1 to 100: "))
        computer_number = random.randint(1, 100)

        if your_number == computer_number:
            print("Success!")
        else:
            print(f"Your number:{your_number}, Random Number:{computer_number}.")
    except ValueError:
        print("Oops! Please enter a valid number between 1 and 100.")
#call the function
random_numero()

#exercise 5: create a random shirt!
'''describes a shirt size and message with default values'''
def make_shirt(size="large", text="I love Python!"):
    return f'The size of the shirt is {size} and the text is {text}.'
print(make_shirt())
print(make_shirt("medium"))
print(make_shirt("tiny","No Message Dude"))

#exercise 6 - list of magician names
#create a list of names
magician_names =['Harry Houdini', 'David Blaine', 'Criss Angel']
'''function takes the magician_names list as a parameter'''
def show_magicians(magician_names):
    for x in magician_names:
        print(x)
show_magicians(magician_names)

#create a function to modify the list
'''modifies the list'''
def make_great(magician_names):
    for x in magician_names:
        i = magician_names.index(x)
        magician_names [i] = x + " The Great"
    return(magician_names)
show_magicians(make_great(magician_names))

#Exercise 7 - Temp advice
#create a function
import random
'''function returns random integer between -10 and 40C'''
def get_random_temp():
    return random.randint(-10,40)
#call it
print(get_random_temp())

#create another function to store it
'''getting the random temp function and storing result'''
def main():
    random_temp = get_random_temp()
    print(f'The temperature right now is {random_temp} degrees Celsius.')
    
    if random_temp < 0:
        print("Brrr, that is freezing! Wear some extra layers today.")
    elif random_temp >= 0 and random_temp<16:
        print("Nice weather.")
    elif random_temp >= 16 and random_temp<23:
        print("A bit warm, stay hydrated.")
    elif random_temp >=23 and random_temp<=40:
        print("It is really hot! Stay cool.")
#calls it
main()

#now let's modify it (bonus)!
import random
'''function returns random floating point  between -10 and 40C'''
def get_random_temp():
    return random.uniform(-10,40)
main()



