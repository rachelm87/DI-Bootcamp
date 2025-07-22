#Write code that asks the user for a number and determines whether this number is odd or even.
number = input('Please enter a number: ')
number = int(number)
if number % 2 == 0:
    print("This number is even")
else:
    print ("This number is odd")