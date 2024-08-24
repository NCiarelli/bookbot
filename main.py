import string

def main():

    print("hello world")

    # Get entire book as a string
    filepath = "books/frankenstein.txt"
    book_name = "Frankenstein"
    book_string = get_book_string(filepath)

    # Count the words in the book
    num_words = count_words(book_string)
    # print(f"Word count of {book_name}: {num_words}")
    
    # Count the characters in the book and create a dictionary of the counts
    char_count_dict = get_char_count_dict(book_string)
    # print(char_count_dict)

    # Generate and print a book stats report
    sorted_letter_list = get_sorted_letter_list(char_count_dict)
    print(sorted_letter_list)
    


def get_sorted_letter_list(char_count_dict):
    
    def sort_on(dict):
        return dict["count"]
    letter_list = []
    for char_key in char_count_dict:
        if char_key.isalpha():
            letter_list.append({"letter": char_key, "count": char_count_dict[char_key]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
    

def get_char_count_dict(book_string):
    book_lower = book_string.lower()
    # print(string.ascii_lowercase)
    count_dict = {}
    for char in book_lower:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def get_book_string(filepath):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_words(book_string):
    return len(book_string.split())
        
        



main()