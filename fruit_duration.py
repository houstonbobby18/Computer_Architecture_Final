import sqlite3

class fruit_table:
    def __init__(self):
        self.database_name = 'fruits_duration'
        self.conn = sqlite3.connect(f'{self.database_name}.db')
        self.cursor = self.conn.cursor()
        
    def get_all_fruits(self):
        self.cursor.execute('SELECT * FROM fruits_duration')
        return self.cursor.fetchall()
    
    def get_columns(self):
        self.cursor.execute('PRAGMA table_info(fruits_duration)')
        return self.cursor.fetchall()
    
    def find_fruit(self, fruit):
        self.cursor.execute('SELECT * FROM fruits_duration WHERE fruit = ?', (fruit,))
        fruit_row = self.cursor.fetchall()
        if len(fruit_row) == 0:
            return 'Fruit not found'
        else:
            return fruit_row
        
    def find_fruit_duration(self, fruit_name):
        fruit_row = self.find_fruit(fruit_name.lower())
        if fruit_row == 'Fruit not found':
            return 'Fruit not found'
        else:
            fruit_values = fruit_row[0][3:-1]
            fruit_means = ["Days on Counter", "Days in Pantry", "Days in Fridge", "Days in Freezer"]
            fruit_duration = dict(zip(fruit_means, fruit_values))
            return fruit_duration
        
    def get_duration_values(self, fruit_name):
        fruit_row = self.find_fruit(fruit_name.lower())
        if fruit_row == 'Fruit not found':
            return 'Fruit not found'
        else:
            fruit_values = fruit_row[0][3:-1]
            return fruit_values
        
if __name__ == '__main__':
    fruit = fruit_table()
    #print(fruit.get_all_fruits())
    print(fruit.get_columns())
    print(fruit.find_fruit('apple'))
    print(fruit.find_fruit_duration('apple'))
    print(fruit.get_duration_values('apple'))
    fruit.conn.close()