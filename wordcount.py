# import sys to pass arguments in the command line
import sys
import re
import collections

#Set argument at index 1 in command line to filename
filename = sys.argv[1]


words = re.findall(r'\w+', open('test.txt').read().lower())
print(collections.Counter(words))

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
            current_word = word_count.get(word, 0)

            #Determine if word is not capitalized and does not end in punct
            if word[0].islower() == True and word[-1].isalpha() == True:

                #If so, add to word_count
                word_count[word] = current_word + 1 

            #Determine if word is capitalized and does not end in punctuation
            elif word[0].isupper() == True and word[-1].isalpha() == True:

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
                word_count[lower_word_no_end] = word_count.get(lower_word_no_end, 0) +1

            #Code below is first attempt to delete bad words afterwards
        
            #Determine if word in word_count is capitalized
            #if word[0].isupper() == True:

                #If so, delete word
                #del word_count[word]
                
                #Determine if word is capitalized and ends in punctuation
                #if word[-1].isalpha() == False:

                    #If so, continue
                    #Don't need to delete again
                    #continue

            #Determine if word ends in puntuation and is not capitalized
            #elif word[-1].isalpha() == False:

                #If so, delete word
                #del word_count[word]

    #Return dictionary of word_count sorted by key only

    #for k, v in sorted(word_count.items()):

        #print(k, v)

    #Return dictionary of word_count sorted:
    #Descending by value
    #Ascending by key
    #sort_word_count = sorted(word_count.items(), key = lambda x: (-x[1], x[0]))

    #Set variable word_items for items in word_dict (list of tuples)
    word_items = word_count.items()

    #Lambda function to sort by descending order for value and
    #Ascending order for key
    word_key = lambda x: (-x[1], x[0])

    #Sort word_items by lambda function
    sort_word_count = sorted(word_items, key = word_key)

    #Loop through sort_word_count
    for tuple in sort_word_count:
        
        #Print key and value at each tuple
        print(tuple[0], tuple[1])



#Run count_words function
count_words(filename)

