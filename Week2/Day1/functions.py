#FUNCTIONS

#a function is a reusale block of code that runs when you "call" it

#Syntax

def func_name(): 
    '''prints a string on the console'''
    print('I am a function')

func_name()

#create a function that prints "Hello there!", then call the function to see the output

def greetings ():
    '''prints "Hello there''' #doc string
    print ('Hello there!')

greetings()

# Passing ARGUMENTS to the function
def greetings_adv(language, name):
    '''prints a greeting depending on the language'''
    if language == 'PT':
        print (f'Ola {name}, tudo bem?')
    
    elif language == 'ES':
        print(f'Hola {name}, que tal?')

    else:
        print('Unknown language')

greetings_adv('ES', 'Dolores')

# key word arguments

def greetings_adv(language, name):
    '''prints a greeting depending on the language'''
    if language == 'PT':
        print (f'Ola {name}, tudo bem?')
    
    elif language == 'ES':
        print(f'Hola {name}, que tal?')

    else:
        print('Unknown language')
greetings_adv(name = 'Pedro', language = 'PT')

#Default value arguments
def greetings_adv(language='EN', name = 'John'):

    '''prints a language namegreeting'''
    if language == 'PT':
        print (f'Ola {name}, tudo bem?')
    
    elif language == 'ES':
        print(f'Hola {name}, que tal?')

    elif language == 'EN':
        print(f'Hi {name}, how are you?')
    else:
        print('Unknown language')

greetings_adv()

#returning values from a function
def calculation(num1, num2):
    '''sums 2 inputted numbers'''
    result = num1+num2
    return result

def multiply(calc):
    '''takes a number and multiples by 5'''
    result = calc * 5
    return result

calc = calculation(5,3)
print(multiply(calc))

def greetings_adv(language='EN', name = 'John'):

    '''prints a greeting to the name, depending on the language '''
    if language == 'PT':
        return f'Ola {name}, tudo bem?'
    
    elif language == 'ES':
        return f'Hola {name}, que tal?'

    elif language == 'EN':
        return f'Hi {name}, how are you?'
    else:
        return 'Unknown language'

greetings_adv()

#create a function called country_info
def country_info (country):
    '''returns the capital of a given country'''
    if country == 'Russia': 
            return 'Moscow'
    elif country == 'Brazil':
        return 'Brasilia'
    elif country == 'Naboo':
        return 'Theed'
    else:
        return 'unknown country'
    
print (country_info('Naboo'))


#global and local scope

age = 25
def current_age():
    print(age)
    my_age = 35
    my_age += 1

current_age()

def happy_birthday():
    # global age
    # age += 1

    if age > 12:
        print("You have bat-mitzvah ")
        age +=1

happy_birthday()
