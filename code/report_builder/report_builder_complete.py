
def print_book_report(word_count, letter_count):
    
    print(str(word_count) + " words found in the document")
    
    print("--------")
    
    for i, j in letter_count.items():
        print(f"the '{i}' character was found {j} times")
        
    print("--------")
    
    ## to continue 