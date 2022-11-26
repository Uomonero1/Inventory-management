"""
Management of a warehouse inventory with Python and SQLite3
"""

import sqlite3
from classes import Connector
from database import create_table

# connection to the database
conn = sqlite3.connect("inventory.db")

def menu():
    print("\nWelcome to the inventory management system")
    while True:
        print("""
        ---------------------------------------------
        \n  Choose an option:
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

            match choice:
                case 1: # INSERT
                    product_name = input("Name: ").strip().lower().replace(" ", "_")
                    while True:
                        try:
                            quantity = abs(int(input("Insert the quantity: ")))
                            break
                        except ValueError:
                            print("Insert numeric values.")
                    department = input("Department: ").strip().lower().replace(" ", "_")
                    product = Connector(name=product_name, quantity=quantity, department=department)
                    product.insert()
                    
                case 2: # UPDATE
                    product_update = input("What product do you want to update? ").strip().lower().replace(" ", "_")
                    while True:
                        try:
                            quantity = abs(int(input("Insert the quantity: ")))
                            break
                        except ValueError:
                            print("Insert numeric values.")
                    department = input("Insert the department: ")
                    product = Connector(name=product_update, department=department, quantity=quantity)
                    product.update()

                case 3: # CHECK THE INVENTORY
                    product = Connector()
                    product.display()

                case 4: # DELETE
                    delete_name = input("What product do you want to delete? ").strip().lower().replace(" ", "_")
                    product = Connector(name=delete_name)
                    product.delete()

                case 5: # SEARCH BY WORD
                    search_word = input("Search: ").strip().lower().replace(" ", "_") + "%"
                    product = Connector(search_word=search_word)
                    product.search()

                case 6: # EXPORT
                    product = Connector()
                    product.export()

                case 7:
                    return False

        except ValueError:
            print("Insert a number from 1 to 7.")


if __name__ == "__main__":
    create_table()
    menu()
    conn.close()

