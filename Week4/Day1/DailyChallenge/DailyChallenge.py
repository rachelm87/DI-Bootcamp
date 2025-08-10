import random
#Part 1 - Quizz
# What is a class?
    ## A defined data type that includes local methods / properties, for
    # object-oriented programming. Unlike functions, classes contain 
    # both data (variables) called properties and methods (functions defined inside a class).
#What is an instance?
    ##A specific object created from a class. 
    # Example: If Dog is the class, dog1 is an instance.# 
#What is encapsulation? 
    ##Encapsulation restricts access to methods and variables to prevent us from
    # directly modifying the data. We mark this by using single underscore (protected/internal) 
    # or double underscore (protected).
#What is abstraction?
    #hiding of information or abstracting away information and giving access to only what’s necessary.
#What is inheritance?
    #when a class takes properties of another class; improves the reuse of existing code. 
#What is multiple inheritance?
    #when a class inherits from more than one parent class; 
    # the order of the parent class in a class definition will decide what is inherited. 
#What is polymorphism?
    #It provides a standard interface for multiple forms or data types (i.e. different or related classes use the same names for their functions). 
#What is method resolution order or MRO?
    ##he order in which Python looks through classes to find a method or attribute.


#Part Two- Create a deck of cards

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'Your card is a {self.value} of {self.suit}'
    
suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "K"]

#card1 = Card("Hearts", "2")
#print(card1)

class Deck: 

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = []
        for suit in suits:
            for value in values:
                new_card = Card(suit, value)  # create a Card object
                self.cards.append(new_card)

    def shuffle(self):
        """Shuffle the cards in the deck."""
        if len(self.cards) == 52:  # only shuffle if full deck
            random.shuffle(self.cards)
        else:
            print("Not a full deck.")
    
    def deal(self):
        '''Takes a single card from deck; after dealt, card is removed'''
        card = random.choice(self.cards) # pick a card
        self.cards.remove(card) #removes from deck
        return card

#deck = Deck()
#deck.shuffle()
#card1 = deck.deal()
#print(card1)
