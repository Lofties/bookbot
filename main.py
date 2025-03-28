import sys
from stats import word_count, char_count, build_report, sort_dict_as_list

def main():
    args = sys.argv
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #file path to the text
    book_path = args[1] 
    
    #reads the text into a string
    text = get_book_text(book_path)
    
    #counts the words in our string
    num_words = word_count(text)

    #counts each char
    book_char_count = char_count(text)

    # # Deprectiated old formatting
    # #converts the text to lower case and then counts each char
    # lowered_text = text.lower() - redundant, moved into function
    
    #creates a sorted list of chars based on the number of occuraances (largest to smallest)
    sorted_list = sort_dict_as_list(book_char_count)
        
    #produces a report, including the book path, number of words and char counts
    build_report(book_path, num_words, sorted_list)

# returns the text as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()