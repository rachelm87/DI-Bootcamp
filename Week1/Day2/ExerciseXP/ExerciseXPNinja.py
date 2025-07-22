#ExerciseXPNinja 1
# print hello world 4x and i love python 4x in one line of code
first_phrase = "Hello World "
second_phrase = "I love python "
print((first_phrase*4) + (second_phrase *4))

#ExerciseXPNinja 2
#insert a month
input_month = int(input("Enter the number of your favorite month (i.e. JAN = 1, FEB = 2, MAR = 3, etc): "))
#check which month it is
if input_month >= 3 and input_month <= 5:
    print("This is Spring.")
elif input_month >= 6 and input_month <= 8:
    print("This is Summer.")
elif input_month >= 9 and input_month <= 11:
    print("This is Autumn.")
elif input_month >=12 and input_month <=2:
    print("This is Winter.")
else:
    print("You did not insert an actual number of a month!!")