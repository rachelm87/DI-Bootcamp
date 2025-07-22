user_name = 'Juliana'
email = 'juliana@gmail.com'
user_age = 35
is_online = True

user_info = [user_name, email, user_age, is_online]
#check length
print(len(user_info))

some_list = list ('item 1')
#create a list with the function
other_list = ['item 1', 'item 2']
print(some_list)
print(other_list)

empty_list = []

#ordered means can be accesed by index
print(user_info[2])

fruits =['orange', 'kiwi', 'apple', 'lime']
#slice
print(fruits[-2:])
fruits[1] = 'pineapple'
print(fruits)

my_name = 'Juliana'
#TypeError: not possible to change an item on a string: strings are immutable my_name [3] = 'e' 

#list methods
fruits =['orange', 'kiwi', 'apple', 'lime']
fruits.insert(1, 'mango')
print(fruits)

fruits.remove('kiwi')
print(fruits)

fruits.append('watermelon')
print(fruits)

fruits.pop(1) #with no argument it deletes the last element
print(fruits)


vegs = ['tomate', 'potato', 'carrot']
colors = ['red', 'blue', 'green']

fruits.extend(vegs)
print(fruits)


#sorted() and .sort()
fruits_sorted = sorted(fruits)
print(fruits)
print(fruits_sorted)

#exercise1
list1 = [5,10,15,20,25,50,20]
#find value 20 on the list

if 20 in list1:
    index_20 = list1.index(20)
    list1[index_20] = 200
print(list1)