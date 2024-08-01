import counters.count_specific_word
import counters.specific_word_counter
import counters.word_count
import counters.word_instance_count
import counters.letter_instance_count
import report_builder.report_builder_basic
import report_builder.report_builder_complete
import utilities
import utilities.get_book
import report_builder

def bookbot_terminal_app(books_file_path):
    print()
    print("Welcome to your Bookbot, \nplease choose from one of the available titles using the associated number: \n(i.e /Book.txt <number>)")
    print()

    for i in range(len(books_file_path)):
        print(str(books_file_path[i]) + " = " + str(i))
        
    print()
    book_selection = input()
    book_text = utilities.get_book.get_book_text(books_file_path[int(book_selection)])
    word_instance_count = counters.word_instance_count.count_instances_of_word(book_text)  
    print()
    
    print(f"Great,'{str(books_file_path[int(book_selection)])}' it is. \nWould you like to: \n > Find and count particular instances of a word (1)? \n > Generate a report from the selected book? (2)")
    print()
    
    action_selection = input()
    print()

    if int(action_selection) == 1:
        while True:
            print("Type the word, be weary of grammar.")
            word_to_find = input()
            result = counters.count_specific_word.find_specific_word_count(word_instance_count, word_to_find)
            print(result)
            
            print("Any other word you're interested in finding? (Y/N)")
            new_selection = input()
            
            if new_selection.lower() == "n":
                print("Thanks, Closing application, goodbye.")
                break  
            elif new_selection.lower() == "y":
                continue 
            else:
                print("Invalid choice, please type 'y' or 'n'.")
    elif int(action_selection) == 2:
        # ask for type of reportas
        print()
        print("Would you like a basic report (1) or a complete one (2)")
        print()
        report_choice = input()
        print()
        
        if int(report_choice) == 1:
            word_count = counters.word_count.book_word_count(book_text)    
            letter_count = counters.letter_instance_count.count_instances_of_letters(book_text)
            report_builder.report_builder_basic.print_basic_book_report(word_count, letter_count);
        elif int(report_choice) == 2:
            report_builder.report_builder_complete.print_complete_book_report();