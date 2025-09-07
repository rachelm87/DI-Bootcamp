import random

#LOOPS: FOR AND WHILE

#for <variable> in <sequence>

#what are the sequences that we know in python?
# STRINGS
for char in 'Student':
    print(char)

# LISTS, SETS AND TUPLES
fruits = ['apple', 'banana', 'watermelon']
for fruit in fruits:
    print(f'I love {fruit}')

# DICTIONARY
#  - keys()
#  - values()
#  - items()

student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 14,
    'address' : 'Privet Drive, 4',
    'pets': ['Hedwig', 'Buckbeak'],
    'houses': {'main': 'Griffyndor', 'second': 'Slytherin'},
    'best_friends': ('Ron Weasley', 'Hermione Granger')
}

# for k in student_info.keys():
#     print(k)

# for v in student_info.values():
#     print(v)

# for k, v in student_info.items():
#     print(k, v)


# RANGE
for i in range(1, 16):
    print(i)

#ENUMERATE
fruits = ['apple', 'banana', 'watermelon']
for fruit in fruits:
    if fruit == 'banana':
        fruit = 'kiwi' #that way I am changing the element just on the loop (not on the sequence)
    print(f'I love {fruit}')

fruits = ['apple', 'banana', 'watermelon']
for enumerate_tupple in enumerate(fruits):
    if fruit == 'banana':
        fruits[i] = 'kiwi' 
    print(f'I love {fruit}')

fruits.insert(1, 'kiwi')
print(fruits)


#WHILE LOOPS


toppings = []


while True:
    top = input("Enter the toppings you want or 'q' to finish: ")
    if top == 'q':
        break
    toppings.append(top)
    
print(f'Thanks for choosing us. Thos are the toppings: {toppings}')

#WGILE + FLAG

game_continue = True

while game_continue:
    guess = int(input('guess a number between 1 and 50: '))
    computer_num = random.randint()

    if guess == computer_num:
        print('Congrats you won!')
        game_continue = False #the flag is changed on the loop
    else:
        print(f'Sorry, wrong guess, the num was {computer_num}')
    
