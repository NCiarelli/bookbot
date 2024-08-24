def main():

    with open("books/frankenstein.txt") as f:
        # ...
        print("hello world")
        book_string = f.read()
        words = book_string.split()
        print(f"Word length of Frankenstein: {len(words)}")



main()