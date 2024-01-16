from Card import Card
from Deck import Deck

'''
Note: DO NOT MODIFY THIS FUNCTION. If your grid is not displaying properly, check your code first or contact us. 

displays a grid of cards arranged in 7x5 col/row formatted like this:
[   [row1, row2, row3...],  <-col1
    [row1, row2, row3...],  <-col2
    [row1, row2, row3...],  <-col3
    ...
]

params:
    grid - a 2D list in the format shown above

returns:
    None (output from this function is printed)

'''
def displayGrid(grid):

    #generate and display the index header for the grid
    headerStr = ""
    for row in range(7):
        headerStr += " \t" + str(row) + "\t "
    print(headerStr)
    print()

    #proces through each of the rows in reverse because we need to print top to bottom (ie last index to first)
    for row in range(4, -1, -1):

        #generate the full string for a row before printing it
        rowStr = "|\t"
        for col in range(7):
            #create an index offset so that cards are always aligned at the top
            offset = 5 - len(grid[col])
            rowIdx = row - offset

            #as long as the row index is valid, get the data for that particular card
            if(rowIdx >=0):
                rowStr += str(grid[col][rowIdx]) + "\t|\t"
            
            #otherwise print an empty space
            else:
                rowStr += "  \t|\t"
            
        #print the completed row and a row separator
        print(rowStr)
        print()

'''
Initializes a grid of cards for golf solitaire

params:
    deck - an instance of the deck class to draw cards from

returns:
    a 2D list of card objects formatted in a 7x5 configuration for 7 columns and 5 rows
'''
def initGrid(Deck):
    '''This function gets the deck() instance we created, 
    and returns a 2D list of objects formatted in 7x5 grids.'''

    grid = []

    ## Use the nested for loop. Create a 2D list and how do we use for loops to create a 2D list. 
    row_count = 0 
    while row_count < 5:
        row = []
        col_count = 0 
        for col in range(7):
            card = Deck.drawCard()
            row.append(card)
            col_count += 1

        grid.append(row)
        row_count += 1

    return grid



'''
Checks whether the grid is empty (ie the grid is a list containing only empty lists). Example is below:

    [ [], [], [], [], [], [], [] ] <--- This grid is empty
    [ [Card, Card], [], [], [Card], [], [], [] ] <--- This grid is NOT empty

params:
    grid - a 2D list in the format shown above

returns:
    True if the grid is empty
    False if the grid is not empty

'''
def checkWin(grid):
    '''This function gets a grid - a 2D list, and gives True if the grid is empty 
    and False if the grid is not empty. '''
    for row in grid:   ## Go through each row in the grid. 
        ## if the row was not empty return False. 
        if row:
            return False
    ## if all the row are not empty return True.   
    return True

'''
Calculates the abs between the values of two cards
params:
    card1 - instance of the Card class
    card2 - instance of the Card class

returns:
    the absolute value between the two cards (accounting for A/J/Q/K)

'''
def compareCards(card1, card2):
    '''This function gets two cards from the deck, and gives the absolute value between the two cards. '''

    ## If one card is 13 and one card is 1, we want to use an if statement to cover that condition. 
    card1_val = card1.getValue()
    card2_val = card2.getValue()

    if card1_val == 13 and card2_val == 1:
        return 1 
    elif card1_val == 1 and card2_val == 13:
        return 1
    
    absolute_value = abs(card1_val - card2_val)
    return absolute_value


'''
Main game function

params:
    none

returns:
    none

'''
def main():
    shuffle_cards = Deck()
    shuffle_cards.drawCard()

    #-This variable dispalys the grids with instructions of the game. 
    cards_grid = initGrid(shuffle_cards)

    #-Initializing a condition of end of the game would allow the user choose to proceed or not. 
    endOfGame = False
    '''This while loop would display grids of the card and check if the user wins or not. '''
    while not endOfGame:
        displayGrid(cards_grid)

        #-The game ends if the player finishes all the cards and there is no card left. 
        if checkWin(cards_grid):
            print("Dear player, You Won!")
            endOfGame = True
        #-The game ends if the player chooses to quit after the user is prompted for an input. 
        else:
            answer = input("What would you like to do next? (Continue/Quit)")
            #-If the player chooses to continue the game would resume. 
            if answer == "Continue":
                pass
            #-If the player chooses to quit, this line would be displayed in terminal. 
            elif answer == "Quit":
                print("Good Performance! Have a nice day!")
                endOfGame = True 

    
if __name__ == "__main__":
    main()

