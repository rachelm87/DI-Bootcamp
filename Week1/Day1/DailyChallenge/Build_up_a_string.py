#ask user to insert a string
your_input = input("Please type something here: ")

if len(your_input) < 10:
    print("String not long enough. ")
elif len(your_input) > 10:
    print("String too long. ")
else: 
    print("Perfect string. ")

#now next step to if perfect print first and last characters
if len(your_input) ==10:
    print(your_input[:9:8])

#let's make a loop!
for i in range(1, len(your_input) + 1):
    print(your_input[:i])