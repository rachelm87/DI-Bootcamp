
#ex 3 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove "Banana" from the list.

# basket.remove("Banana")


# Remove "Blueberries" from the list.
# basket.remove("Blueberries")


# Add "Kiwi" to the end of the list.
# basket.append('Kiwi')


# Add "Apples" to the beginning of the list.
# basket.insert(0, 'Apples')

# Count how many times "Apples" appear in the list.
# basket.count('Apples')


# Empty the list.
# print(basket.clear())

# Print the final state of the list.
# print(basket)

#conclusion: methods are called in the following syntax:
# data-type/ data-structure.method_name()

# Recap: What is a float? What’s the difference between a float and an integer?
# float is a basic data type for decimal number


# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?


# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# numbers = []
# for number in range(1, 6):
#     numbers.append(number)
#     float_num = number + 0.5
#     numbers.append(float_num)

# print(len(numbers))
# print(numbers[1:-1])

nums2 = []
for i in range(1, 21):
    # print(i)
    nums2.append(i)

print(nums2)
for i in nums2:    
    if nums2.index(i) % 2 == 0:
        print(i)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

favorite_fruits = []

for fruit in basket:
    favorite_fruits.append(f'I love {fruit}')

print(favorite_fruits)


# while <condition>:
#   indented block of code
#   check condition

# user_name = input('Enter your name')

# while user_name != 'Juliana':
#     user_name = input('Enter your name')

# a better way for the while loop syntax:


while True:
    user_name = input('Enter your name')
    if user_name == 'Juliana':
        break