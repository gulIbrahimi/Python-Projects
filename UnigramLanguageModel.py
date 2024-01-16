# Project 3 ---

## Unigram Model --> Language Model

'''Already Given Function to incorporate.'''

## Function 1 :
def readWordFromText(fileName):
    '''This function opens the requested file and returns the text in it as a list of individual words'''
    J_FairyTale = open("/Users/gulamizibrahimi/Desktop/Third Semester/Language Model/JapaneseFairyTales.txt", "r")
    txt_file = J_FairyTale.read().split() 
    return txt_file

## Function 2 :
def makeWordList(words):
    '''This function gets a list of words, and returns a list of unique words.'''
    '''It's purpose is to remove repetition in words.''' 
    unique_words = [] 
    for word in words: 
        '''use a for loop to go through each element of the words.''' 
        if word not in unique_words:
            unique_words.append(word) 
    return unique_words
    
## Function 3 :
def getIndexOfWord(wordList, word):
    '''This function gets a wordlist, and returns the index of 'word' inside 'wordList'.'''
    for i in range(len(wordList)):
        if wordList[i] == word:
            return i 
    return -1

## Function 4 :
def createEmptyList(length):
    '''Creates and returns a list of zeros with the specified length.'''
    empty_array = [0] * length
    return empty_array
    

# Function 5 :
def computeDistribution(origText, wordList):
    '''This function computes the probability distribution of words used in a text.'''
    '''It gets two arguments (origText, wordList) and gives out a list of floats of the percentage of distribution.'''
    words = len(origText)
    word_counts = createEmptyList(len(wordList))

    for word in origText:
        '''We go through each element in origText, and find the if the word is inside the wordList (our list without repetition).'''
        if word in wordList:
            index = wordList.index(word)
            word_counts[index] += 1 

    distribution = []

    for count in word_counts:
        '''if there were any words found, we then divide the number of their appearance by the total amount of words.'''
        if words > 0:
            distribution.append(count / words) 
        else:
            distribution.append(0) 
    return distribution
    

# Function 7)
def computeProbability(wordList, dist, sentence):
    '''This function returns the probability that the “sentence” appears in a text (modeled by wordList and dist). '''
    words_in_sentence = sentence.split()
    probability = 1.0
    
    for word in words_in_sentence:
        word_index = getIndexOfWord(wordList, word)

        if word_index != -1:
            probability *= dist[word_index]
        else:
            probability *= 1 / len(wordList)

    return probability

# Function 8)

def main():
    fileName = "/Users/gulamizibrahimi/Desktop/Third Semester/Language Model/JapaneseFairyTales.txt"
    origText = readWordFromText(fileName)
    wordList = makeWordList(origText)
    dist = computeDistribution(origText, wordList)
    answer = input("Do You Want to Make a Guess? (Yes/No): ").lower()
    while answer == "yes":
        sentence = input("Enter a sentence to compute probability: ")
        probability = computeProbability(wordList, dist, sentence)
        print(probability)
        answer = input("Do You Want to Make a Guess? (Yes/No): ").lower()
 
   

if __name__ == "__main__":
    main()