def count_num_words(book):
    total_book = book.split()
    count_words = 0

    for words in total_book:
        count_words += 1


    return count_words



def count_each_char(book):
    char_counts = {}
    
    book_to_lower = book.lower()
    
    for i in range(0, len(book_to_lower)):
        char = book_to_lower[i]
        
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts 



def sort_counts(char_counts):
    sorted = []

    for key in char_counts:
        num_count = char_counts[key]
        new_dict = {"char": key, "num": num_count}

        sorted.append(new_dict)


    def sort_on(sorted):
        return sorted["num"]

    sorted.sort(reverse=True, key=sort_on)

    return sorted