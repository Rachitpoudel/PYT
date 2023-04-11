books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year of publication: "))
    book = {"title": title, "author": author, "year": year}
    books.append(book)
    print("Book added successfully.")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in books:
        if book["title"] == title:
            books.remove(book)
            print("Book removed successfully.")
            break
    else:
        print("Book not found.")

def search_by_title():
    title = input("Enter the title of the book to search for: ")
    found_books = []
    for book in books:
        if book["title"].lower() == title.lower():
            found_books.append(book)
    if found_books:
        print(f"{len(found_books)} book(s) found:")
        for book in found_books:
            print(f"{book['title']} by {book['author']}, published in {book['year']}")
    else:
        print("No books found.")

def search_by_author():
    author = input("Enter the author of the book to search for: ")
    found_books = []
    for book in books:
        if book["author"].lower() == author.lower():
            found_books.append(book)
    if found_books:
        print(f"{len(found_books)} book(s) found:")
        for book in found_books:
            print(f"{book['title']} by {book['author']}, published in {book['year']}")
    else:
        print("No books found.")

def list_all_books():
    print("List of all books:")
    for book in books:
        print(f"{book['title']} by {book['author']}, published in {book['year']}")

def quit_program():
    print("Exiting the program.")
    quit()

menu = {
    1: add_book,
    2: remove_book,
    3: search_by_title,
    4: search_by_author,
    5: list_all_books,
    6: quit_program
}

while True:
    print("Welcome to the library inventory program!")
    print("Please choose an option:")
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. Search for a book by title")
    print("4. Search for a book by author")
    print("5. List all the books")
    print("6. Quit")
    choice = int(input("Enter your choice (1-6): "))
    if choice not in range(1, 7):
        print("Invalid choice. Please choose again.")
        continue
    menu[choice]()
