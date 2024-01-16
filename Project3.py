## Project 3 ---

## Unigram Model --> Language Model


'''Already Given Function to incorporate.'''

## Function 1 :

## readWordsFromText(fileName): 
## This function opens the requested file and returns the text in it as a list of individual words.
    ## It takes 1 argument: fileName (string) - the name of the file you want to open and read the text from.
    ## It returns a list of strings. Each string is one word.


def readWordFromText(fileName):
    '''This function opens the requested file and returns the text in it as a list of individual words'''
    
    J_FairyTale = open("/Users/gulamizibrahimi/Desktop/Third Semester/Language Model/JapaneseFairyTales.txt", "r")

    # Next, read in the file contents
    # readlines reads the whole file into a list, where each element contains 1 line of the file
    txt_file = J_FairyTale.read()
    
    # we then split files with spaces. 
    split_lines = txt_file.split()

    print(fileName)

    # Close tells your computer you're done working with this file
    J_FairyTale.close()

    return split_lines


## Function 2 :

## makeWordList(words): 
## This function returns a list containing all of the unique words inside of the list “words” (i.e., removes all repeats in “words”).
    ## It takes 1 argument: words (list) - a list containing all of the words in a text
    ## It returns a list of strings. Each string is one word.

def makeWordList(words):
    '''This function gets a list of words, and returns a list of unique words.'''
    '''It's purpose is to remove repetition in words.''' 
    unique_words = [] # make an empty array of unique words.

    wordList = words.split()

    for word in wordList: # use a for loop to go through each element of the words. 
        
        if word not in unique_words:
            unique_words.append(word)

    return unique_words


    # for word in words: # use a for loop to go through each element of the words. 
    #     unique_words_found = 0
    #     for unique_word in unique_words:

    #         if word == unique_word:
    #             unique_words_found += 1
    #             break

    #     if unique_words_found:
    #         unique_words.append(word)

    # return unique_words


## Function 3 :

## getIndexOfWord(wordList, word): 
## This function returns the index of “word” inside of the list “wordList”
    ## It takes 2 arguments:
    ## wordList - a list of strings to search inside of word - a string to search for
    ## It returns an integer representing the index of word inside of wordList or -1 if the word does not appear.

def getIndexOfWord(wordList, word):
    '''This function gets a wordlist, and returns the index of 'word' inside 'wordList'.'''

    ## We start the index by -1, because we already have 0 in our list. 
    IndexOfWord = -1  

    for i in range(len(wordList)):
        if wordList[i] == word:
            IndexOfWord = i
        else:
            IndexOfWord = IndexOfWord + i  

    return IndexOfWord

## Function 4 :

## createEmptyList(length): 
## This function creates and returns a list of the specified length containing only 0s.
    ## It takes 1 argument - length (integer): the desired length of the list.
    ## It returns a list of the specified length, containing only 0s.

def createEmptyList(length):
    '''Creates and returns a list of zeros with the specified length.'''

    empty_array = [0] * length

    return empty_array
    

## computeDistribution(origText, wordList):
## This function computes the probability distribution of words used in a text, 
# that is: If you picked a word at random, what’s the probability that you pick a specific word? 
# For instance, for the phrase “I know that you know”, there is a:
    # 1 in 5 (20%) chance you pick the word “I”, 
    # 1 in 5 (20%) chance you pick the word “you”,
    # 1 in 5 (20%) chance you pick the word “that”, and
    # 2 in 5 (40%) chance you pick the word “know”
## This function takes 2 arguments:
    # origText: A list of strings - The text from one book. Each element of the list is a single word.
    # wordList: A list of strings - The list of all words that appear in the text (with no repeats)
    # This function returns a list of floats.
    # The length of the returned list should be the same length as the list passed in as wordList. 
    # The ith element of the returned list should correspond to the proportion of the text which the ith word of wordList was.
    # For example: 
        # If wordList = [“all”, “dogs”, “are”, “good”], returning the list [0, 0.75, 0, 0.25] indicates that:
        #  “all” and “are” never appear in the text origText,
        # “dogs” represents 75% of the words in origText, and
        # “good” represents 25% of the words in origText.

def computeDistribution(origText, wordList):
    '''This function computes the probability distribution of words used in a text.'''
    '''It gets two arguments (origText, wordList) and gives out a list of floats of the percentage of distribution.'''
    word_counts = []
    words_array = len(origText)

    ## We can go through each element of the wordList one by one. 
    ## 
    for word in wordList:
        word_counts[word] = 0 

    for word in origText:
        if word in word_counts:
            word_counts[words] = 1

    distribution = []
    for word in wordList:
        if words_array > 0:
            distribution.append(word_counts[words] / words_array)
        else:
            distibution.append(0)

    return distribution

# computeProbability(wordList, dist, sentence):
    # This function returns the probability that the “sentence” appears in a text (modeled by wordList and dist). 
    # This function takes 3 arguments:
        # wordList: A list of strings - A list of all words that appear in the text (with no repeats)
        # dist: A list of floats - The probability distribution of the words in wordList (i.e., element i of dist is the probability associated with the ith word of wordList). 
        # sentence: A string - the sentence you want to predict the probability for.
    # This function returns 1 float representing the probability of the sentence occurring. 
    # The probability that any sentence appears is equivalent to the product of the probabilities of each of its words. 
    # For example, the probability of the sentence “computers love bytes” appearing is equivalent to:
    # (probability of “computers”) * (probability of “love”) * (probability of “bytes”)    
    # Many of the words entered by the user will appear in the original text (and therefore wordList). 
    # But what if a word entered by the user doesn’t appear?
    # If the word entered by the user doesn’t appear in wordList, 
    # you should assign it a probability of 1/(length of wordList). 

# Note: The result of this function will often be a very small number so don’t be worried if you see python format these numbers in scientific notation when printed like this: 

def computeProbability(wordList, dist, sentence):
    '''This function returns the probability that the “sentence” appears in a text (modeled by wordList and dist). '''
    '''It takes three arguments(wordList, dist, sentence) and returns 1 float representing the probability of the sentence occurring.'''

    words_in_sentence = sentence.split() # We split the sentence by the words, to find the distribution. 

    probability = 1.0 # We set the initial probability to 0.1
   
    '''We use a for loop in order for us to go through each word in our words' list.'''
    for word in words_in_sentence:
        
        ## If the word was included in our wordlist, we find its index or position in our sentence. 
        if word in wordList:
            word_index = wordList.index(word)

            '''probability finds the word index and the distance element associated with each other.'''
            ## It then multiplies it to continue updating the value. 
            probability *= dist[word_index]
        else:
            '''if we have an unknown word, we simply assign it a default value.'''
            probability *= 1 / len(wordList)

    return probability 



# main():
# This is the main function which puts all of the pieces together. 
# The flow of your main method (and thus the program as a whole) will be:
def main():
    pass

if __name__ == "__main__":
    main() 