"""
Management of a store inventory with Python and SQLite3
"""

# TODO: esportazione su csv, excel di tutta o una parte del database
# TODO: pubblicare su GitHub

import sqlite3
from classes import Connector
import csv

# connection to the database
conn = sqlite3.connect("inventory.db")

def menu():
    choice = None
    while choice != 7:
        print("""
        \n-------------------------------------------------------
        \nWelcome to the inventory management system. Choose an option
        \n1 | Add a product
        \n2 | Update the quantity of a chosen product
        \n3 | Check the inventory
        \n4 | Delete a product
        \n5 | Search a product
        \n6 | Export the database to a CSV file
        \n7 | Exit
        """)

        try:
            choice = int(input("What do you want to do? "))
        except ValueError:
            print("Insert a number from 1 to 5.")

        if choice == 1: # INSERT
            product_name = input("Name: ").strip().lower().replace(" ", "_")
            quantity = abs(int(input("Insert the quantity: ")))
            department = input("Department: ").strip().lower().replace(" ", "_")
            product = Connector(name=product_name, quantity=quantity, department=department)
            product.insert()
            
        elif choice == 2: # UPDATE
            product_update = input("What product do you want to update? ").strip().lower().replace(" ", "_")
            quantity = int(input("Insert the quantity: "))
            department = input("Insert the department: ")
            product = Connector(name=product_update, department=department, quantity=quantity)
            product.update()

        elif choice == 3: # CHECK THE INVENTORY
            product = Connector()
            product.display()

        elif choice == 4: # DELETE
            delete_name = input("Which object do you want to delete? ").strip().lower().replace(" ", "_")
            product = Connector(name=delete_name)
            product.delete()

        elif choice == 5: # SEARCH BY WORD
            search_word = input("Search: ").strip().lower().replace(" ", "_") + "%"
            product = Connector(search_word=search_word)
            product.search()

        elif choice == 6: # EXPORT
            product = Connector()
            product.export()

if __name__ == "__main__":
    menu()
    conn.close()

