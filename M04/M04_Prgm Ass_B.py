# 16.8

import sqlalchemy
from sqlalchemy import text

conn = sqlalchemy.create_engine('sqlite:///books.db')

with conn.connect() as connection:
    result = connection.execute(text("SELECT title FROM book ORDER BY title ASC"))
    rows = result.fetchall()

for row in rows:
    print(row[0])