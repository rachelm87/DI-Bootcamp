#Challenge 1: Sorting - Write a Python program that takes a single string of words 
# as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). 
# The program should output these words sorted in alphabetical order, 
# with the sorted words also separated by commas.
random_phrase = input("Insert several words then press 'Enter: ")
split_str = random_phrase.split( )
split_str.sort()
join_str = ",".join(split_str)
print(join_str)

#Challenge 2: Longest Word
#Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.

'''function takes string (sentence) as parameter'''
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
your_long_sentence = input("Please type in a sentence here, then press 'enter': ")
answer = longest_word(your_long_sentence)
print("The longest word is:", answer)