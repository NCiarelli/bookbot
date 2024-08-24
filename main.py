import string

def main():

    print("hello world")

    # Get entire book as a string
    filepath = "books/frankenstein.txt"
    book_name = "Frankenstein"
    book_string = get_book_string(filepath)

    # Count the words in the book
    num_words = count_words(book_string)
    print(f"Word count of {book_name}: {num_words}")
    
    # Count the characters in the book and create a dictionary of the counts
    char_count_dict = get_char_count_dict(book_string)
    print(char_count_dict)

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