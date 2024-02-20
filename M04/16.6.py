import sqlite3

db = sqlite3.connect('books.db')
curs = db.cursor()

sql = 'select title from book order by title asc'

for row in db.execute(sql):
    print(row[0])