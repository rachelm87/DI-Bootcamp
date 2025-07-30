#FUNCTIONS and DATA StRUCtuRES

students =['Harry', 'Ron', 'Hermione', 'Luna']

#create a function that says Name, welcome to Hogwarts for each one of the students of teh given list

def welcome():
    for name in students:
        print(f'(name), welcome to Hogwarts')

welcome()

def get_house():
    for i, name in enumerate(students):
        students[i] = f'(name) - Gryffindor'

get_house()
print(students)
