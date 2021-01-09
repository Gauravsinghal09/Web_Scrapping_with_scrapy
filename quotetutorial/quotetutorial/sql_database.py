import sqlite3

conn = sqlite3.connect('my_quotes.db')

curr = conn.cursor()

curr.execute("""create table quote_tb(
                title text,
                author text,
                tag text
)""")

curr.execute("""insert into quote_tb values(
                'Practice makes a man perfect', 'Wise Man', 'Pyscology'
)""")

conn.commit()

conn.close()