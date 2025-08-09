import os
import random

#EXERCISE 1: RANDOM SENTENCE GENERATOR

#step 1 - read this file
dir_path = os.path.dirname(os.path.realpath(__file__)) #will search directory for file
print('dir path: ', dir_path)

file_path = os.path.join(dir_path, 'words.txt') #define it for the function

#function created to read this delightful file

def get_words_from_file (file_path, length = 10): #updated this for the main function so that it doesnt hardcode the number
    with open(file_path, 'r', encoding='utf-8') as f: #this now knows what the variable is (Defined earlier))
        file_content = f.read()
        words = file_content.split() #this ensures that you don't print just the 10 characters as python reads it all like one long list of characters. 
        #length = 10 see above
        random_sentence = []
        for i in range(length):
            word =random.choice(words) #you don't need the += sign here 
            random_sentence.append(word)
        format_sentence = ' '.join(random_sentence).lower()
    return(format_sentence) #don't use print 

print(get_words_from_file(file_path)) #you need the file_path so it doesn't call the function — it just prints out the function object itself.

#step 2 - create main function

def main():
    message = input(f"This program generates a random sentence of a specified length from a word list.\n You will decide the next sentence length. Insert a number between 2 and 20: ")
    if not message.isdigit(): #validating the user's input (is it an integer?)
        print(f'Bummer, game over')
        exit()
    number = int(message)    #okay its a digit, now let's convert to a number
    if number >20 or number <2: #is it within range? 
        print(f'Number is not within range.')
        exit()
    
    your_sentence = get_words_from_file(file_path, number) 
    #finally, we can create teh sentence!
    return(f'You created a new sentence with {number} words: {your_sentence} !')

print (main())

#Exercise 2 - Access a nested key in a JSON string, add a new key, and save
# the modified JSON to a file.

import json
import os
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}""" #added two missing double quotes to close it

parsing_dict= json.loads(sampleJson) # parsing json string into python dictionary
print(parsing_dict)

#access nested salary key and print it
#for key, value in parsing.items():
    #print(key, type(value)) # this wasn't helpful so let's try another way

# List of keys to traverse the dictionary
keys = ["company", "employee", "payable", "salary"]
# Accessing the nested value using a loop to get salary
salary = parsing_dict
for key in keys:
    salary = salary.get(key) # key exists thats why you need to remove {}
    
print(salary)

#add the new "birth_date value key"
parsing_dict["company"]["employee"]['birth_date'] = '1987-11-28' #had a mistake here so i had to insert company and employee before going straight to adding birth_date
print(parsing_dict)

#save json to the file
dir_path = os.path.dirname(os.path.realpath(__file__)) #will search directory for file
file_path = os.path.join(dir_path, 'ExerciseXP2.json')

with open(file_path, 'w', encoding='utf-8') as f: #this now knows what the variable is (Defined earlier))
    json.dump(parsing_dict, f, indent =2)

