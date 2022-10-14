import sqlite3
import pandas as pd
import csv

class Connector:
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    def __init__(self, name: str = None, quantity: int = None, department: str = None, search_word: str = None):
        self.name = name
        self.quantity = quantity
        self.department = department
        self.search_word = search_word

    # inserts the given product with quantities and department into the db
    def insert(self):
        # checks the db if the product already exists
        self.cursor.execute("""
            SELECT Name
            FROM Store
            WHERE Name=?
        """, (self.name,))
        result = self.cursor.fetchone()

        if result:
            print("There is already a product with that name in the table. Check the inventory.")
        else:
            self.cursor.execute("""
                INSERT INTO Store (Name, Quantity, Department)
                VALUES (?,?,?)
            """, (self.name, self.quantity, self.department))
            self.conn.commit()

    # updates the quantity of a product
    def update(self):
        # checks if the product is in the db
        self.cursor.execute("""
            SELECT Name
            FROM Store
            WHERE Name=?
        """, (self.name,))
        result = self.cursor.fetchone()

        if result:
            self.cursor.execute("""
                UPDATE Store 
                SET Quantity =?, Department=? 
                WHERE Name =?
            """, (self.quantity, self.department, self.name))
            self.conn.commit()
        else:
            print("This product isn't in the table.")
        
    # deletes a product from the db
    def delete(self):
        # checks if the product is in the db
        self.cursor.execute("""
            SELECT Name
            FROM Store
            WHERE Name=?
        """, (self.name,))
        result = self.cursor.fetchone()

        if result:
            self.cursor.execute("""
                DELETE FROM Store
                WHERE Name = ?;
            """, (self.name,))
            self.conn.commit()
        else:
            print("This product isn't in the table.")

    # searches for a product in the db
    def search(self):
        self.cursor.execute("""
            SELECT *
            FROM Store
            WHERE Name LIKE ?
        """, (self.search_word,))
        result = self.cursor.fetchone()

        if result:
            print(pd.read_sql_query("""
            SELECT *
            FROM Store
            WHERE Name LIKE ?
            """,
            self.conn,
            params=(self.search_word,)))
        else:
            print("This product doesn't exist.")

    # displays the all inventory or a chosen part
    def display(self):
        # checks if the inventory is empty
        self.cursor.execute("SELECT * FROM Store")
        result_1 = self.cursor.fetchone()
        
        if result_1:
            answer = input("Do you want to display all the products in the inventory?(y/n) ").strip().lower()
            if answer == "y":
                print(pd.read_sql_query("SELECT * FROM Store WHERE Quantity > 0", self.conn))

            else:
                # checks if the given department exists
                selected_department = input("What departement do you want to display? ").strip().lower().replace(" ", "_")
                self.cursor.execute("SELECT Department FROM Store WHERE Department=?", (selected_department,))
                result = self.cursor.fetchone()

                # displays product from the chosen department
                if result:
                    print(pd.read_sql_query("""
                    SELECT * 
                    FROM Store 
                    WHERE Department=?""", 
                    self.conn, 
                    params=(selected_department,)))
                else:
                    print("There is no such department in the table. Check your spelling.")
        else:
            print("There is nothing in the table. Add something to display.")
    
    # exports the entire database to a csv file
    def export(self): 
        file_name = input("Insert the name of the output file: ").strip().lower().replace(" ", "_")
        file_name = file_name + ".csv"
        sequence = self.cursor.execute("SELECT * FROM Store")
        
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(["Name", "Department", "Quantity"])
            for line in sequence:
                writer.writerow(line)