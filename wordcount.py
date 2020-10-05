# import sys to pass arguments in the command line
import sys

#Set argument at index 1 in command line to filename
filename = sys.argv[1]

def count_words(file_name):
    """Return a dictionary of the count of words in a text.

    Values stored as lower-case words:
    - Capitalized words will be counted as lower-case words
    - Punctuation will be stripped from text
    """
    #Open file_name, store as variable file
    file = open(file_name)

    #Create empty dictionary named word_count
    word_count = {}

    #Loop through each line in the file
    for line in file:

        #Strip white space at the end of each line
        line = line.rstrip()

        #Split each line on the space
        lst_of_line = line.split(' ')

        #Loop through each word in each line
        for word in lst_of_line:

            #Add word to dictionary word_count
            word_count[word] = word_count.get(word, 0) + 1 

            #Determine if word is capitalized and does not end in punctuation
            if word[0].isupper() == True and word[-1].isalpha() == True:

                #Create variable called lower_word
                #Lower first letter of word and concatenate with rest of word
                lower_word = word[0].lower() + word[1:]

                #Add lower_word to word_count
                #If lower_word not in word_count, add to word_count
                word_count[lower_word] = word_count.get(word, 0) + 1
                
            #Determine if word ends in punctuation and is not capitalized 
            elif word[-1].isalpha() == False and word[0].isupper() == False:

                #Add word without punctuation to word_count
                word_count[word[0:-1]] = word_count.get(word, 0) + 1

            #Determine if word is capitalized AND ends in punctuation
            elif word[0].isupper() == True and word[-1].isalpha() == False:

                #Create variable called lower_word_no_end
                #Lower first letter of word and concatenate w/o punctuation
                lower_word_no_end = word[0].lower() + word[1:-1]

                #Add lowercase word with no punctuation to word_count
                word_count[lower_word_no_end] =
                word_count.get(lower_word_no_end, 0) +1
        
            #Determine if word in word_count is capitalized
            if word[0].isupper() == True:

                #If so, delete word
                del word_count[word]
                
                #Determine if word is capitalized and ends in punctuation
                if word[-1].isalpha() == False:

                    #If so, continue
                    #Don't need to delete again
                    continue

            #Determine if word ends in puntuation and is not capitalized
            elif word[-1].isalpha() == False:

                #If so, delete word
                del word_count[word]

    #Return dictionary of word_count
    return word_count

#Call count_words function
print(count_words(filename))