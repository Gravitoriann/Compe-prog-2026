## This is the template for 2D2, full problem in the rulebook ##

def solve(books: list[str]):
    """
    Create the library with the book organized

    Parameters:
        books list[str]: The books to organize in the library

    Returns:
        list[str]: The library visualized
    """
    library = []
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##
    books.sort()
    books.sort(key=lambda item:len(item))
    books = books[::-1]
    active = True
    len_max_book = len(books[0])+2
    len_list = len(books[0])
    len_sl = len(books) + (len(books)-1) + 2
    books_with_spaces = []
    for book in books:
        for i, letter in enumerate(book):
            if i == 0:
                if len_max_book-len(book):
                    spaces = "_"*(len_max_book-len(book)+1)
                    new_book_str = spaces + book+"_"
                    books_with_spaces.append(new_book_str)
                else:
                    books_with_spaces.append("_"+book+"_")
    for row in range(len_list):
        sous_str = ""
        for book in books_with_spaces:
            if len(book) != 1:
                if book[0] == "_" and book[1] != "_":
                    sous_str+= "┌───┐"
                else:
                    sous_str+=f"│ {book[0]} │"
            else:
                sous_str+="└───┘"
            book = book[1:]


    return library