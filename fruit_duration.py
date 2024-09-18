import sqlite3

databese_name = 'fruits_duration'
# Load the database
print(f"Loading {databese_name}.db database...")
connectiion = sqlite3.connect(f'{databese_name}.db')
cursor = connectiion.cursor()
print(f"{databese_name}.db database loaded")

def connect():
        connectiion = sqlite3.connect(f'{databese_name}.db')
        cursor = connectiion.cursor()
class Fruit:
    def __init__(self, fruit):
        self.fruit = fruit.lower()
        try:
            self.fruit_data = Fruit.get_fruit(fruit.lower())
            self.counter_storage = Fruit.get_counter_storage(self.fruit_data)
            self.panty_storage = Fruit.get_panty_storage(self.fruit_data)
            self.refrigerator_storage = Fruit.get_refrigerator_storage(self.fruit_data)
            self.freezer_storage = Fruit.get_freezer_storage(self.fruit_data)
            self.notes = Fruit.get_notes(self.fruit_data)
        except:
            raise ValueError(f"{fruit} is not in the {databese_name}.db database")

    def get_fruit(fruit):
        query = f"SELECT * FROM fruits_duration WHERE Fruit = '{fruit}'"
        cursor.execute(query)
        return cursor.fetchall()

    def get_counter_storage(fruit):
        days = int(fruit[0][3])
        return days

    def get_panty_storage(fruit):
        days = int(fruit[0][4])
        return days

    def get_refrigerator_storage(fruit):
        days = int(fruit[0][5])
        return days

    def get_freezer_storage(fruit):
        days = int(fruit[0][6])
        return days

    def get_notes(fruit):
        notes = fruit[0][7]
        if notes == 'None':
            return None
        else:
            return notes
    
    def __str__(self):
        return f"Fruit: {self.fruit}\nCounter Storage: {self.counter_storage}\nPanty Storage: {self.panty_storage}\nRefrigerator Storage: {self.refrigerator_storage}\nFreezer Storage: {self.freezer_storage}\nNotes: {self.notes}"
    
if __name__ == "__main__":
    fruit = Fruit("apple")
    print(fruit)
    try:
        fruit = Fruit("beef")
    except ValueError as e:
        print(e)
