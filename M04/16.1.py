import csv
text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''
with open('books.csv', 'wt') as outfile:
    outfile.write(text)