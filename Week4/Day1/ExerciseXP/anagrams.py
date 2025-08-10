import os
#part two

from anagram_checker import AnagramChecker

def main():
    here = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(here, "sowpods.txt")
    confirming = AnagramChecker(file_path)

    while True:  # loop forever unless user leaves
        print("\n--- ANAGRAM CHECKER ---")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Type 1 or 2: ").strip()

#user decides
        if choice == "2":
            print("Goodbye!")
            break

        if choice != "1":
            print("Please type 1 or 2.")
            continue

#user inputs
        word = input("Enter a word: ").strip() 

        if " " in word:
            print("One word only. ")
            continue 
        if not word.isalpha():
            print("Letters only. ")
            continue
        if not confirming.is_valid_word(word):
            print(f'Your word: {word} is not a valid English word.')
            continue

    #now checking anagrams
        anagrams = confirming.get_anagrams(word)
        print("Your word:", word.upper())
        if anagrams:
            print("Anagrams:", ", ".join(anagrams))
        else:
            print("No anagrams found.")
