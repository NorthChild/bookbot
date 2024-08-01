def find_specific_word_count(dictionary, word_to_find):
    
    if word_to_find in dictionary:
        count = dictionary[word_to_find]
        result = "Word: '" + str(word_to_find) + "', found " + str(count) + " times in the book."
        return result