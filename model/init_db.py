import sqlite3
connection = sqlite3.connect('snake.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

    cur = connection.cursor()

cur.execute("INSERT INTO snake (score) values(1000)")
cur.execute("INSERT INTO snake (score) values(1000)")

connection.commit()
connection.close()