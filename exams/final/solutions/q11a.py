from library import books

#
# QUESTION 11-A
#

# SOLUTION

matching_books = [book for book in books if book["id"] == 4]
matching_book = matching_books[0]
print(matching_book["title"])

# ALSO CORRECT

matching_books = []

for book in books:
    if book["id"] == 4:
        matching_books.append(book)

matching_book = matching_books[0]
print(matching_book["title"])

# ALSO CORRECT

for book in books:
    if book["id"] == 4:
        print(book["title"])
