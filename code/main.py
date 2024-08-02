import counters
import counters.count_specific_word
import counters.letter_instance_count
import counters.word_count
import counters.word_instance_count
import user_journey.user_selection
import utilities
import utilities.get_book
import report_builder
import report_builder.report_builder_basic
import user_journey

def main():
    
    books_file_path = ["books/frankenstein.txt", "books/greek_tragedy.txt", "books/he_who_served.txt", "books/independance_day.txt"] 
    
    book_text = utilities.get_book.get_book_text(books_file_path[3])
    # print(book_text)
    
    # word_count = counters.word_count.book_word_count(book_text)    
    # letter_count = counters.letter_instance_count.count_instances_of_letters(book_text)
    # word_instance_count = counters.word_instance_count.count_instances_of_word(book_text)
    
    # specific_word_count = counters.count_specific_word.find_specific_word_count(word_instance_count, input())
    # print(specific_word_count)
    
    # print report
    # report_builder.report_builder_basic.print_basic_book_report(word_count, letter_count)

    user_journey.user_selection.bookbot_terminal_app(books_file_path)

        

main()