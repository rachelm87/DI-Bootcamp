#ExerciseXP1

#create "hello world" 4x 
print ("Hello world \n" *4)

#now print output into one line of code
print ("Hello world " *4)

#ExerciseXP2

#write a code that calculates a result
print((99**3)*8)

#ExerciseXP3
#predict the output of the following

#false
print (5 < 3)
#true
print (3 == 3)
#false
print (3 == "3")
#typeerror
print ("3" > 3)
#false
print ("Hello" == "hello")

#ExerciseXP4
#create a variable called a computer brand

computer_brand = "Mac"

#print a sentence

print(f"I have a {computer_brand} computer.")

#ExerciseXP5

#create a variable name
my_name = "Rachel"

#create a variable age

my_age = "37"

#create a variable shoe size
my_shoe_size = "38"

#create a variable called info
my_info = f"My name is {my_name} and I am {my_age} and I buy size {my_shoe_size} EU."

#print it!
print (my_info)

#ExerciseXP6
#create two variables
variable_a = 37
variable_b = 36

#now create a conditional
if variable_a > variable_b: 
    print("Hello World")
    
#ExerciseXP7
#Write code that asks the user for a number and determines whether this number is odd or even.
number = input('Please enter a number: ')
number = int(number)
if number % 2 == 0:
    print("This number is even")
else:
    print ("This number is odd")
    
#ExerciseXP8
#do we have the same name?
#confirming my name
my_name="Rachel"

#asking for your name
input("What's your name? ")
print(input)

#does your name = my name?
your_name = input("What's your name? ")
if your_name == my_name:
    print("Our names are great!")
else:
    print("too bad!")

#ExerciseXP9

#Write code that will ask the user for their height in centimeters.

your_height = input("Please tell me your height in CM ")
your_height =int(your_height)

#now determine if they can ride it!
if your_height > 145:
    print ("You are tall enough to ride this ride!")
else: 
    print ("Sorry Charlie! Gotta grow some more!") 
