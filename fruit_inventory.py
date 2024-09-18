import sqlite3
import os
import time




def create_table(database_name):
    if os.path.exists(database_name):
        return
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE inventory
                 (id INTEGER PRIMARY KEY, name TEXT, date_added INTEGER, expiration_date INTEGER, picture_name TEXT, real_fruit TEXT)''')
    conn.commit()
    conn.close()



database_name = 'inventory.db'
print(f"Loading {database_name} database...")
if not os.path.exists(database_name):
    create_table()
print(f"{database_name} database loaded")


def connect():
   conn = sqlite3.connect(f'{database_name}.db')
   c = conn.cursor()


def get_unixtime():
    return int(time.time())

def convert_unixtime_to_date(unixtime):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unixtime))

def add_days_to_unixtime(unixtime, days):
    return unixtime + (days * 86400)



def add_item(picture_name, expiration_date_delta, name, real_fruit):
    current_time = get_unixtime()
    expiration_date = add_days_to_unixtime(current_time, expiration_date_delta)
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO inventory (name, date_added, expiration_date, picture_name, real_fruit) VALUES (?, ?, ?, ?, ?)", (name, 0, current_time, expiration_date, picture_name, real_fruit))
    conn.commit()
    conn.close()

def get_item(id):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE id=?", (id,))
    item = c.fetchone()
    conn.close()
    return item

def get_all_items():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    items = c.fetchall()
    conn.close()
    return items

def get_expired_items():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE expiration_date < ?", (get_unixtime(),))
    items = c.fetchall()
    conn.close()
    return items

def get_expiring_items(days):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE expiration_date < ?", (add_days_to_unixtime(get_unixtime(), days),))
    items = c.fetchall()
    conn.close()
    return items

def get_items_by_name(name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory WHERE name=?", (name,))
    items = c.fetchall()
    conn.close()
    return items


