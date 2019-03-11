from library import books

#
# QUESTION 11-A
#

# SOLUTION

older_books = [book for book in books if book["year"] < 1990]

print(len(older_books))

# ALSO CORRECT

older_books = []

for book in books:
    if book["year"] < 1990:
        older_books.append(book)

print(len(older_books))
