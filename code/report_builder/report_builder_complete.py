
def print_complete_book_report(book_path, word_count, letter_count, words_counts):
    
    with open("Reports/NewCompleteReport.txt", "w") as f:
        
        print(f"Generated report for {book_path}", file = f)
        
        print("--------", file = f)
        
        print(str(word_count) + " words found in the document", file = f)
        
        print("--------", file = f)
        
        for i, j in letter_count.items():
            print(f"the '{i}' character was found {j} times", file = f)
            
        print("--------", file = f)
        
        for i, j in words_counts.items():
            print(f"the '{i}' word was found {j} times", file = f)
        
        print("--- End of report ---", file = f)