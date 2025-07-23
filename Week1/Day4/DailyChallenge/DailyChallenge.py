#DailyChallenge 1
#Give me two integers
number = int(input("Enter a number: "))
length = int(input("Enter another number for the length: "))
print(number)
print(length)

#put it in a list
totals = []

#create the mulitple
for i in range (1, length + 1):
    total = number * i

    if total > length:
        break

    totals.append(total)
print(totals)

#DailyChallenge2
#input a word
your_word = input("Enter in a word, any word with typos and multiple consecutive letters!: ")
print(your_word)

#start with the word
result = your_word[0]

#print only unique consecutive letters
for i in range(1, len(your_word)):
    add_letter = your_word[i]
    previous_letter = your_word [i-1]

    #is it the same or not?
    if add_letter != previous_letter:
        result = result + add_letter
#tell them!
print(f"I think you meant: {result}")

