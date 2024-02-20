import csv
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book)