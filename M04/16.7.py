import sqlite3

db = sqlite3.connect('books.db')
curs = db.cursor()

for row in db.execute('select * from book order by year'):
    print(*row, sep=', ')