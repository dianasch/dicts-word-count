# put your code here.
import sys

filename = sys.argv[1]

def count_words(file_name):
    file = open(file_name)

    word_count = {}
    for line in file:
        line = line.rstrip()
        lst_of_line = line.split(' ')

        for word in lst_of_line:
            word_count[word] = word_count.get(word, 0) + 1 

            if word[0].isupper() == True and word[-1].isalpha() == True:
                upper_word = word[0].lower() + word[1:]
                word_count[upper_word] = word_count.get(word, 0) + 1
                
            elif word[-1].isalpha() == False and word[0].isupper() == False:
                word_count[word[0:-1]] = word_count.get(word, 0) + 1

            elif word[0].isupper() == True and word[-1].isalpha() == False:
                upper_word_no_end = word[0].lower() + word[1:-1]
                word_count[upper_word_no_end] = word_count.get(upper_word_no_end, 0) +1
        
   
            print(word_count)
        if word[0].isupper() == True:

            del word_count[word]


        

        

    return word_count

print(count_words(filename))