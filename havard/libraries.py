# import random OR
from random import choice
from random import randint
from random import shuffle

def main():
    fruitsList = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    cards = ['King', 'Jack', 'Queen', 'Ace', 'Joker']
    randomChoice(fruitsList)    
    randInt(0, 10)
    randomSuffle(cards)
# end def
    
def randomChoice(list):
    print(choice(list))
# end def
    
# Random numbers between 0 and 10 (inclusive)
def randInt(min, max):
    print(randint(min, max))
# end def

# Shuffle (melanger) the list
def randomSuffle(list):
    shuffle(list)
    print(list)
# end def

def averageNote(list):   
    print(sum(list) / len(list))    
# end def

main()