import sys
from stats import count_words, count_chars, sort_dict
def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")    
    count_words(get_book_text(book_path))
    print("--------- Character Count -------")   
    sorted_dictionary = sort_dict(count_chars(get_book_text(book_path)))
    for entry in sorted_dictionary:
        print(f"{entry["letter"]}: {entry["num"]}")    
    print("============= END ===============")

main()

