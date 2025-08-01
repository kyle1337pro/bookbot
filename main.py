import sys
from stats import (count_num_words, count_each_char, sort_counts)


def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()

        return book_text



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    book = get_book_text(book_path)

    num_words = count_num_words(book)
    char_count = count_each_char(book)

    sorted_report = sort_counts(char_count)

    report_title = "============ BOOKBOT ============"
    word_count_title = "----------- Word Count ----------"
    char_count_title = "--------- Character Count -------"
    end = "============= END ==============="

    print(report_title + "\r")
    print(f"Analyzing book found at {book_path}...\r")
    print(word_count_title + "\r")
    print(f"Found {num_words} total words\r")
    print(char_count_title + "\r")
    
    for counts in sorted_report:
        check_char = counts["char"]
        if str.isalpha(check_char):
            print(f"{counts["char"]}: {counts["num"]}\r")
        
    print(end)


main()