#Create a Text class to analyze text data, either from a string or a file. 
#Then, create a TextModification class to perform text cleaning.
import string
import re

class Text:
    def __init__(self, text):
        self.text = text

#Step 2: Implement word_frequency Method
    def word_frequency (self,word):
        list_of_words = self.text.lower().split()
        count = list_of_words.count(word.lower())
        if count == 0:
            return None
        return count

#Step 3: Implement most_common_word Method
    def most_common_word(self): #nothing new, because you're not passing anything
        frequencies = {}
        words = self.text.lower().split()

        for word in words: 
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1 #storing it
        highest_count = 0
        commonest_word = ""
        for word, count in frequencies.items():
            if count > highest_count:
                highest_count = count
                commonest_word = word
            
        return commonest_word

#Step 4: Implement unique_words Method
    def unique_words(self):
        words = self.text.split() #    Split the text into a list of words.
        unique_set = set(words)
        unique_list = list(unique_set) # Use a set to store unique words.

        return unique_list

#classmethod
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
        return cls(file_content)

class TextModification(Text):
#Step 7: Import String

    def remove_punctuation(self):
        cleaned = ""
        for char in self.text:
            if char not in string.punctuation:
                cleaned += char
        return cleaned

# Step 8: Remove stop words
    def remove_stop_words(self):
        stop_words = {"a", "the", "is", "and", "of", "in", "to"}
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        remaining_words = " ".join(filtered_words)
        return remaining_words

# Step 9: Remove special characters
    def remove_special_characters(self):
        cleaned = re.sub(r"[^A-Za-z0-9\s]", "", self.text)
        return cleaned

if __name__ == "__main__":
    file_path = "HarryPotter.txt"  #harry potter


    text = Text.from_file(file_path)
    print("Word frequency for 'they':", text.word_frequency("they"))
    print("Most common word:", text.most_common_word())
    print("Unique words:", text.unique_words())
    tm = TextModification.from_file(file_path)
    print("\nText without punctuation:\n", tm.remove_punctuation())
    print("\nText without stop words:\n", tm.remove_stop_words())
    print("\nText without special characters:\n", tm.remove_special_characters())