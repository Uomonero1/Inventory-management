import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Store")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Store(
        Name TEXT(30) PRIMARY KEY NOT NULL,
        Department TEXT(20) NOT NULL,
        Quantity INTEGER(5))
    """)
connection.commit()
connection.close()

