import re

def count_instances_of_word(text): 
    words_counts = {}
    lowered_words = []
    pattern = r'[^\w\s]'
    
    split_words = text.split()
    
    for i in split_words:
        # remove non letter characters to the split words using regex
        cleaned_text = re.sub(pattern, '', i)
        lowered_words.append(cleaned_text.lower())
    
    for word in lowered_words:
        if word not in words_counts:
            words_counts[word] = 1
        else:
            words_counts[word] += 1
    words_counts = dict(sorted(words_counts.items(), key=lambda item: item[1], reverse=True))
    return words_counts