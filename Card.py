'''Card_Class'''

## Project 4

'''This class is representing the individual property of each card in the deck. '''
class Card:

    '''Constructor - value, suit. '''
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit 
        
    def __str__(self):
        return(str(self.value) + self.suit)
 
        

def main():
    pass



if __name__ == "__main__":
    main()