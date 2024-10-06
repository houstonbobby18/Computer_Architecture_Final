import sqlite3
import os
import time

def create_database():
    '''
    Database is created with ID, Picture_Name, Exp_Date, Predicted_Fruit, Real_Fruit, and Date_Added columns
    '''
    if os.path.exists('fruits_inventory.db'):
        return 
    conn = sqlite3.connect('fruits_inventory.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE fruits_inventory (ID INTEGER PRIMARY KEY AUTOINCREMENT, Picture_Name TEXT, Exp_Date TEXT, Predicted_Fruit TEXT, Real_Fruit TEXT, Date_Added TEXT)')
    conn.commit()
    conn.close()

def connect_database():
    '''
    Connects to the database
    '''
    conn = sqlite3.connect('fruits_inventory.db')
    cursor = conn.cursor()
    return conn, cursor

def add_fruit(conn, cursor, picture_name, exp_date, predicted_fruit, real_fruit):
    '''
    Adds a fruit to the database and returns the ID of the fruit added
    '''
    date_added = time.strftime('%Y-%m-%d %H:%M:%S') 
    cursor.execute('INSERT INTO fruits_inventory (Picture_Name, Exp_Date, Predicted_Fruit, Real_Fruit, Date_Added) VALUES (?, ?, ?, ?, ?)', (picture_name, exp_date, predicted_fruit, real_fruit, date_added))

    conn.commit()
    # Gets the ID
    cursor.execute('SELECT ID FROM fruits_inventory WHERE Picture_Name = ?', (picture_name,))
    id = cursor.fetchall()[0][0]
    return id

def pop_fruit(conn, cursor, id):
    '''
    Deletes the most recent fruit from the database
    '''
    cursor.execute('DELETE FROM fruits_inventory WHERE ID = ?', (id,))
    conn.commit()
    return 0
    
def get_all_fruits(conn, cursor):
    '''
    Returns all the fruits in the database
    '''
    cursor.execute('SELECT * FROM fruits_inventory')
    return cursor.fetchall()

if __name__ == '__main__':
    # Connect to the database
    create_database()
    conn, cursor = connect_database()

    # Add a fruit
    picture_name = 'test.jpg'
    exp_date = 5
    predicted_fruit = 'apple'
    real_fruit = 'apple'
    id = add_fruit(conn, cursor, picture_name, exp_date, predicted_fruit, real_fruit)
    print(f"Fruit added with ID: {id}")

    # Get all fruits
    fruits = get_all_fruits(conn, cursor)
    print(fruits)

    # Pop a fruit
    pop_fruit(conn, cursor, id)
    print('Fruit popped')

    # Get all fruits
    fruits = get_all_fruits(conn, cursor)
    print(fruits)




