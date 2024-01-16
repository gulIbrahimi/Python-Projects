

# Error 1)
def getInput():
    '''This function gets a string as "Answer", and gives stops the program if it is "No" and continues the program if it is "Yes".'''
    '''If the answer is "YES", it asks for another input for a sentence to compute probability.'''

    answer = input("Do You Want to Make a Guess? (Yes/No): ").lower()

    if (answer == "no"):
        print("The program ends here! Thank you for running our code! ^_^. ")
        return False


    else:
        computeProbability(wordList, dist, sentence)
        
        # return True

    # else:
    #     print("Invalid Input! Please enter either YES or NO.")
    #     return getInput()



# Error 2)

# Get Input from the user: 

def getInput():
    '''This function gets a string as "Answer", and gives stops the program if it is "No" and continues the program if it is "Yes".'''
    '''If the answer is "YES", it asks for another input for a sentence to compute probability.'''

    answer = input("Do You Want to Make a Guess? (Yes/No): ").lower()

    if (answer == "no"):
        print("The program ends here! Thank you for running our code! ^_^. ")
        return False


    elif (answer == "yes"):
        computeProbability(wordList, dist, sentence)
        # second_input = input("Enter a sentence: ").lower()
        return True

    else:
        print("Invalid Input! Please enter either YES or NO.")
        return getInput()


# Error 3)
def computeProbability(wordList, dist, sentence):
    '''This function returns the probability that the “sentence” appears in a text (modeled by wordList and dist). '''
    '''It takes three arguments(wordList, dist, sentence) and returns 1 float representing the probability of the sentence occurring.'''
    sentence = getInput()

    words_in_sentence = sentence.split() # We split the sentence by the words, to find the distribution. 

    probability = 1.0 # We set the initial probability to 0.1
   
    '''We use a for loop in order for us to go through each word in our words' list.'''
    for word in words_in_sentence:
        word_index = getIndexOfWord(wordList, word)  

        if word_index != -1:  
           
            probability *= distribution[word_index]
        else:
            
            probability *= 1 / len(wordList)

    return probability