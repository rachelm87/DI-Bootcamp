#Challenge 1: Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()). 
#User Input: prompt user for a word
word = input("Enter a word: ")
variable_name = word
print(variable_name)

#Create the Dictionary and loop through the word checking if character already a key in dictionary: 
my_dict = {}
for index, char in enumerate(word):
    if char in my_dict:
        my_dict[char].append(index)
    else: 
        my_dict[char] = [index]
    print(f"{char}:{index}", end=" ")
print("\n",my_dict)

#confirm that keys are strings
for key in my_dict:
    print(f"Key: {key}, Type: {type(key)}")

#ensure the values are captured in the list
total_indices = sum(len(value) for value in my_dict.values())
result = len(word)
if total_indices == len(word):
    print(f"The {word} has {result} indices, which equals the {total_indices} in the list. All good.")
else: 
    print(f'Something is wrong. There is s a difference between the number and what is in the list.')

#Challenge Two!
#Create a program that prints a list of items that can be purchased with a given amount of money.

#Step1 - Store Data: 
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

#Step2 - Clean it so that output is : ["Bread", "Fertilizer", "Water"].
for key, value in items_purchase.items():
    clean_value = value.replace("$", "").replace(",", "")
    label_value = int(clean_value)
    items_purchase.update({key: label_value})
print(items_purchase)

clean_wallet = int(wallet.replace("$",""))
print(clean_wallet)

#is this affordable?

affordable_list = []

for key, value in items_purchase.items():
    if value <= clean_wallet:
        affordable_list.append(key)
if not affordable_list:
    print("Nothing") 
else:
    affordable_list.sort()
    print(affordable_list)

#do it again!
items_two_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet_two = "$100"
affordable_two = []

#clean it up!
for key, value in items_two_purchase.items():
    clean_value = value.replace("$", "").replace(",", "")
    label_value = int(clean_value)
    items_two_purchase.update({key: label_value})

clean_wallet = int(wallet_two.replace("$",""))

#is this affordable?
for key, value in items_two_purchase.items():
    if value <= clean_wallet:
        affordable_two.append(key)
if not affordable_two:
    print("Nothing") 
else:
    affordable_two.sort()
    print(affordable_two)

#last test
items_three_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet_three = "$1"
affordable_three = []

#clean it up using shorter code
items_three_purchase = {
    key: int((value.replace("$", "")).replace(",",""))
    for key, value in items_three_purchase.items()
}

clean_wallet = int(wallet_three.replace("$",""))

#try to cost check using shorter code
for key, value in items_three_purchase.items():
    if value <= clean_wallet:
        affordable_three.append(key)
if not affordable_three:
    print("Nothing") 
else:
    affordable_three.sort()
    print(affordable_three)
