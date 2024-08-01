import counters
import counters.count_specific_word
import counters.letter_instance_count
import counters.word_count
import counters.word_instance_count
import utilities
import utilities.get_book
import report_builder
import report_builder.report_builder_basic

def main():
    
    book_file_path = "books/frankenstein.txt"
    
    book_text = utilities.get_book.get_book_text(book_file_path)
    # print(book_text)
    
    word_count = counters.word_count.book_word_count(book_text)
    # print("Found a total of: " + str(word_count) + f" words for {book_file_path}")
    
    # word_instance_count = counters.word_instance_count.count_instances_of_word(book_text)
    # # print("Specific words count: " +str(word_count) + f" for {book_file_path}")
    
    # specific_word_count = counters.count_specific_word.find_specific_word_count(word_count, input())
    # # print(specific_word_count)
    
    letter_count = counters.letter_instance_count.count_instances_of_letters(book_text)
    # print("Letters count: " + str(letter_count) + f" for {book_file_path}")
    
    # print report
    report_builder.report_builder_basic.print_book_report(word_count, letter_count)

    


    # to do
    # add a way to have multiple books 
    # on launch, choose a book
    # add user choice of looking for specific words in the book or print a report (basic or complete)
    # add unit tests 

    
        
        
        

main()