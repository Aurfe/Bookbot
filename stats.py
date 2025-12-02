def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def num_of_words_in_book(file_path):
    text_from_book = get_book_text(file_path)
    list_of_words = text_from_book.split()
    return len(list_of_words)

def book_char_dictionary(file_path):
    text_from_book = get_book_text(file_path)
    dict = {
        'a' : 0,
        'b' : 0,
    }
    list_of_words = text_from_book.split()

    for word in list_of_words:
        for character in word:
            char = character.lower()
            if(char in dict):
                dict[char] += 1
            else:
                dict[char] = 1
    
    return dict

def sorted_dict_list(filepath):
    dict_of_chars = book_char_dictionary(filepath)
    dict_list = []
    for key in dict_of_chars:
        new_dict = {"char" : key, "num" : dict_of_chars[key]}
        dict_list.append(new_dict)
    dict_list.sort(key= return_num_value, reverse= True)
    return dict_list

def return_num_value(dict):
    return dict["num"]