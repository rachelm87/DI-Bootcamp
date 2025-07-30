#ARGS and KWARGS
#ARGS = arguments = lists, tuples, and sets
#key, word arguments = dictionary

students =['Harry', 'Ron', 'Hermione']

def welcome(*args):
    if args:
        for name in args:
            print(f'{name}, welcome!')
    
    else:
        print('you didnt pass names')

#welcome(students)
welcome('Camila', 'Niv', 'Michal', 'David', 'Flavia')

def user_info(**kwargs):
    print(kwargs)

user_info(name = 'Juliana', email = 'ju@gmail.com', age = 35, is_online = True, pets = ['Cat,' 'Dog'])