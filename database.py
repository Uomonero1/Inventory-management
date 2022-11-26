import sqlite3

def create_table():
    connection = sqlite3.connect(".\inventory.db")
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Store")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Store(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Name TEXT(30) NOT NULL,
            Quantity INTEGER(5) NOT NULL,
            Department TEXT(20) NOT NULL
            )
        """)
    connection.commit()
    connection.close()

