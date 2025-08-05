

#Exercise 1 - Currencies: Implement dunder methods for a Currency class to handle string representation, 
# integer conversion, addition, and in-place addition.
#Step 1: 
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'
    
    def __int__(self):
        return int(f'{self.amount}')
    
    def __repr__(self):
        return f"{self.amount} {self.currency}" + ("s") if self.amount != 1 else ""

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError ("This is not compatible")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, int):
            return self.amount + other
        else:
            raise TypeError ("No dice")
        
    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError ("This is not compatible")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError ("No dice")
        return self
        


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))

print(int(c1))
# 5

print(c1)
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

#print(c1 + c3)


#Exercise 2 - 
from func import sum_it
sum_it(1, 3)

#Exercise 3 - 
import string
import random

letters = string.ascii_letters
print(letters)

mix_it_up = ''

for l in range(5):
    random_char = random.choice(letters)
    mix_it_up += random_char
    print(f'This is the random string:', mix_it_up)


#Exercise 4
import datetime
#create a function that displays the current date.
def current_date():
    today = datetime.datetime.now()
    print(f"Today is: ", today.strftime("%B %d %Y"))
current_date()

#Exercise 5 - Amount of time til January 1
#Step 1: Import the datetime module
import datetime

def get_current_datetime():
    return datetime.datetime.now()

today = get_current_datetime()
print(today)

next_year = datetime.datetime(2026, 1, 1, 00, 00, 00)

total_days = next_year - today

print(f"There are {total_days.days} days until 1 January")
print(f"There are {total_days.total_seconds()} seconds until 1 January")

#Exercise 6 - Instructions: Create a function that accepts a birthdate as an argument (in the format of your choice),
#  then displays a message stating how many minutes the user lived in his life

def living():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthday = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.datetime.now()
    difference = today - birthday
    difference_minutes = difference.total_seconds() / 60
    print(f"Thank you! You have lived ", difference_minutes, "minutes since you were born!")

living()