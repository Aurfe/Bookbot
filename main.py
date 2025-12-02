from stats import num_of_words_in_book
from stats import book_char_dictionary
from stats import sorted_dict_list
import sys

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    number_of_words = num_of_words_in_book(filepath)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(filepath) + "...")
    print("----------- Word Count ----------")
    print("Found " + str(number_of_words) + " total words")

    
    dict_list = sorted_dict_list(filepath)

    print("--------- Character Count -------")
    for dict in dict_list:
        if (dict["char"].isalpha()):
            print(str(dict["char"]) + ": " + str(dict["num"]))
    
    print("============= END ===============")


main()