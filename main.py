def main():
    #file path to the text
    book_path = "books/frankenstein.txt"
    
    #reads the text into a string
    text = get_book_text(book_path)
    
    #counts the words in our string
    num_words = word_count(text)

    #converts the text to lower case and then counts each char
    lowered_text = text.lower()
    book_char_count = char_count(lowered_text)
    sorted_list = sort_dict_as_list(book_char_count)
        
    #produces a report, including the book path, number of words and char counts
    build_report(book_path, num_words, sorted_list)

# returns the text as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

#splits the text string into a list of single words and returns the list    
def word_count(word_string):
    word_list = word_string.split()
    return len(word_list)

#counts each character using a dict, returns the dict
def char_count(text):
    char_dict = {}
    for c in text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

# provides the key for the dictionary to be sorted on
def sort_on(dict):
    return dict["num"]

# sorts the given dctionary (chars and nums) into a list of dictionaries sorted on nums. e.g. [{d, 3}, {b, 2}, {a, 1} {c, 0}]
def sort_dict_as_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#using given formatting, displays the path, the number of words and the char counts on seperate lines.
def build_report(book_path, num_words, sorted_list):
    report_start = f"--- Begin report of {book_path} ---"
    words_found = f"{num_words} words found in the document"
    report_end = f"--- End report ---"

    print(report_start)
    print(words_found)
    print()
    for c in sorted_list:
        if c['char'].isalpha():
            print(f"The '{c['char']}' character was found {c['num']} times")
    print()
    print(report_end)


main()