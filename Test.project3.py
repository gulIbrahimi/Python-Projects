# 1)
def readWordFromText(fileName):
    '''This function opens the requested file and returns the text in it as a list of individual words'''
    
    J_FairyTale = open("/Users/gulamizibrahimi/Desktop/Third Semester/Language Model/JapaneseFairyTales.txt", "r")

    # Next, read in the file contents
    # readlines reads the whole file into a list, where each element contains 1 line of the file
    txt_file = J_FairyTale.read()
    
    # split files with spaces. 
    split_lines = txt_file.split()

    print(fileName)

    # Close tells your computer you're done working with this file
    J_FairyTale.close()

    return split_lines


#



# 2)
def getIndexOfWord(wordList, word):
    '''This function gets wordlist and one string, and returns the index of 'word' inside 'wordList'.'''

    ## We start the index by -1, because we already have 0 in our list. 
    IndexOfWord = -1  

    for i in range(len(wordList)):
        if wordList[i] == word:
            IndexOfWord = i
        else:
            IndexOfWord = 0   

    return IndexOfWord


# 3)
def createEmptyList(length):
    '''Creates an empty array and returns a list of zeros with the specified length of indexes.'''

    empty_array = [0] * length

    return empty_array
    

# 4)
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


# 5)
def makeWordList(words):
    '''This function gets a list of words, and returns a list of unique words.'''
    '''It's purpose is to remove repetition in words.''' 
    unique_words = [] # make an empty array of unique words.

    wordList = words.split()

    for word in wordList: # use a for loop to go through each element of the words. 
        
        if word not in unique_words:
            unique_words.append(word)

    return unique_words
    

# 6)
def computeProbability(wordList, dist, sentence):
    '''This function returns the probability that the “sentence” appears in a text (modeled by wordList and dist). '''
    '''It takes three arguments(wordList, dist, sentence) and returns 1 float representing the probability of the sentence occurring.'''
    sentence = input("Enter a sentence: ").lower()

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


# Note: Finding the Index of the Word in wordList:

# Imagine wordList as a list of words from the text. wordList.index(word) tries to find the position (index) 
# where a specific word is located in this list.
# For example, if wordList contains ["apple", "banana", "orange"], 
# wordList.index("banana") would give you the index 1 because "banana" is at position 1 in the list.

# Using the Index to Get Probability from dist:
# dist is another list that contains probabilities associated with the words in wordList. 
# Each element in dist corresponds to a probability for the word at the same index position in wordList.
# So, if wordList has "banana" at index 1, then dist[1] would give you the probability associated with "banana".
# For example, if dist is [0.3, 0.5, 0.2], dist[1] would give you 0.5, 
# which is the probability associated with "banana" in wordList.
# Therefore, when you find the index of a word in wordList and use that index to retrieve a value from dist, 
# it's essentially getting the probability assigned to that particular word in the text.
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


def getInput():
    '''This function gets a string as "Answer", and stops the program if it is "No" and continues the program if it is "Yes".'''
    answer = input("Do You Want to Make a Guess? (Yes/No): ").lower()

    if answer == "no":
        print("The program ends here! Thank you for running our code! ^_^. ")
        return None
    elif answer == "yes":
        return input("Enter a sentence to compute probability: ")
    else:
        print("Invalid Input! Please enter either Yes or No.")
        return getInput()




def computeProbability(wordList, dist, sentence):
    '''This function returns the probability that the “sentence” appears in a text (modeled by wordList and dist). '''
    words_in_sentence = sentence.split()
    probability = 1.0
    
    for word in words_in_sentence:
        word_index = wordList.index(word) if word in wordList else -1

        if word_index != -1:
            probability *= dist[word_index]
        else:
            probability *= 1 / len(wordList)

    return probability


def main():
    pass

    # fileName = "/Users/gulamizibrahimi/Desktop/Third Semester/Language Model/JapaneseFairyTales.txt"
    # origText = readWordFromText(fileName)
    # wordList = makeWordList(origText)
    # dist = computeDistribution(origText, wordList)
    # sentence = getInput()
    # probability = computeProbability(wordList, dist, sentence)
    # print(probability)

    # length = 10 
    # print(createEmptyList(length))


    # wordList = ["happy", "sad", "cute", "mad"]
    # word = "angry"

    # print(getIndexOfWord(wordList, word))


    # # words = "Here is your perfect as it should be here. "
    # # print(makeWordList(words))
    # wordList = ["gul", "loves", "linghe"]
    # dist = [0.2, 0.3, 0.5]


    # sentence_1 = "computers love bytes"
    # result_1 = computeProbability(wordList, dist, sentence_1)
    # print(result_1)

    # # Test 2: Word not in wordList
    # sentence_2 = "gul loves linghe"
    # result_2 = computeProbability(wordList, dist, sentence_2)
    # print(result_2)


if __name__ == "__main__":
    main() 