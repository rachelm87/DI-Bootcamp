import os

#Mini Project #Anagram Checker

#step 1 - read this file
dir_path = os.path.dirname(os.path.realpath(__file__)) #will search directory for file
print('dir path: ', dir_path)

file_path = os.path.join(dir_path, 'sowpods.txt') #define it for the function

class AnagramChecker: 
#creating function to read this file
    def __init__(self, file_path):
        self.word_list = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                self.word_list.append(word)
    
    def is_valid_word(self, word): #checks if this word is in the list 
        word = word.strip().lower()
        if word in self.word_list:
            return True
        else:
            return False
        
    def is_anagram (self, word1, word2):
        word1 = word1.lower() #making sure capitalization doesn't ruin it
        word2 = word2.lower()

        if word1 == word2:
            return False
        return sorted(word1) == sorted(word2)
    
    def get_anagrams(self, word): #find all anagrams for the given word.
        anagrams = []
        for thisword in self.word_list:
            if self.is_anagram(word, thisword):
                anagrams.append(thisword)
        return anagrams
