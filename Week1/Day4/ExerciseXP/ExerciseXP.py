#Exercise1
print("\033c")

#create a set
my_fav_numbers = {7, 9, 21, 25, 29, 37, 43, 101}
print(my_fav_numbers)

#add two numbers
my_fav_numbers.update ({1,100})
print(my_fav_numbers)

#remove last number
my_fav_numbers.remove(100)
print(my_fav_numbers)

#create a list with friend's favorite numbers and combine them
friend_fav_numbers = {6, 12, 18, 24, 36}
print(friend_fav_numbers)
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise2
#create a tuple of integers
my_tuple = (3,6,9,12)
print(my_tuple)

#add more
#my_tuple object has no attribute 'append' 'remove' 'add' or 'update' changes cannot be made which protect it from further modification

#Exercise3
#create a list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

#remove
basket.remove ("Banana")
basket.remove ("Blueberries")
print(basket)

#add
basket.append ("Kiwi")
basket.insert (0, "Apples")
print(basket)

#count
count_apples=basket.count("Apples")
print(count_apples)

#empty the list!
basket.clear()
print(basket)

#Exercise4
#float has decimal while integer is an entire / whole number
numbers = []

for i in range (1,9): #i had to increase because the range grew when i divided rather than 1,6
    numbers.append((1)+(i/2))
    print(numbers)

#Exercise5

#for loop printing numbers in range 1 to 20
for numbers in range (1,21):
    print(numbers)

#now print only even items
for numbers in range (2,21,2):
    print(numbers)

#Exercise7
#input your fave fruit
fruits = input("What are some names of fruit? Enter these here and separate with a space: ")
print(fruits)

#ask them again
new_fruit = input ("What is your favorite fruit?")
print(new_fruit)

#compare
if new_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise 9
#how many people and their age? 
number_people = int(input("How many people are going to the movie? "))
print(number_people)
total_cost= 0
for i in range (number_people):
    old = int(input(f"Enter Person {i+1}'s age: "))
    print(old)

#add a conditional to calculate the loop totals
    if old < 3:
        price = 0
    elif 3 <= old <= 12:
        price = 10
    else:
        price = 15

    total_cost=total_cost + price
#total me

print(f"Your total is $: {total_cost}")