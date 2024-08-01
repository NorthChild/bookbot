import re 

def count_instances_of_letters(text):
    letter_counts = {}
    
    for letter in text: 
        lowered_letter = letter.lower()
        if letter.isalpha():
            if lowered_letter not in letter_counts:
                letter_counts[lowered_letter] = 1
            else:
                letter_counts[lowered_letter] += 1
            
    sorted_dict = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict