import random
from Card import Card


class Deck:
    def __init__(self):
        """it gets an empty list and generates a list from 1 to 52 cards."""
        self.cards = []
        self.generateDeck()
        self.shuffle()


    def generateDeck(self):
        """generates a deck of un-shuffled cards"""
        """which generates the 52 Card instances in the deck, stores them in a list, 
        and “stores” that list as a property of the instance."""
        for suit in ["♠", "♣", "♥", "♦"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle(self):
        """This method shuffles the cards and picks out random cards from the deck."""

        for i in range(150):

            # declare a variable called index1 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
            index1 = random.randint(0, len(self.cards) - 1)
            # declare a variable called index2 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
            index2 = random.randint(0, len(self.cards) - 1)
            # declare a variable called temp and assign it to the element of the deck of Cards located at index1
            temp = self.cards[index1]
            # set the element of the deck of Cards located at index1 to the element of the deck located at index2
            self.cards[index1] = self.cards[index2]
            # set the element of the deck of Cards located at index2 to temp
            self.cards[index2] = temp

    def drawCard(self):
        """draws a card from the deck and return a card object"""
        '''This method gets the shuffled cards and gives a card randomly. '''
        if len(self.cards) > 0:
            drawn_card = self.cards.pop(0)
            return drawn_card
        else:
            return None

    """
    returns the number of cards left in the deck as an int
    """
    def cardsLeft(self):
        """This method gets the drawn cards and subtract them from the total cards,
        it, then, returns the number of cards left in the deck as an integer."""
        remaining_cards = len(self.cards) 
        return remaining_cards


def main():
    pass 


    
if __name__ == "__main__":
    main()
