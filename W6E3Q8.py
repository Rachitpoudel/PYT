books = [
    ("The Hck ", "Prakash shrestha"),
    ("Muna Madhan", "Laxmi prassad devkota"),
    ("1984", "George Orwells"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("Pride and Prejudice", "Jane Austen")
]

sorted_books = sorted(books, key=lambda x: x[1])

print(sorted_books)
