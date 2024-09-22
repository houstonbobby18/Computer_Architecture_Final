import time
import os

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from fruit_duration import fruit_table
import fruit_inventory
import inferencing

def preform_inference(file_path):
    print(f"Running inference on {file_path}")
    fruit_name = inferencing.run_model(file_path)
    print(f"Detected fruit: {fruit_name}")
    real_fruit = input("Is the detected fruit correct? (y/n): ")
    if real_fruit == 'n':
        real_fruit = input("What is the real fruit name?: ")
    else:
        real_fruit = fruit_name
    return fruit_name, real_fruit

    
class FruitEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.queue = []
    def on_created(self, event: FileSystemEvent):
        if event.is_directory:
            return
        if not event.src_path.endswith(".jpg"):
            return
        self.queue.append(event.src_path)


def main():
    observer = Observer()
    event_handler = FruitEventHandler()
    if not os.path.exists("./images_processed"):
        os.makedirs("./images_processed")
    observer.schedule(event_handler, "./images_processed", recursive=False)
    observer.start()
    queue = []
    fruit_duration_table = fruit_table()
    print(fruit_duration_table.get_columns())
    try:
        while True:
            queue.extend(event_handler.queue)
            event_handler.queue.clear()
            time.sleep(1)
            if len(queue) > 0:
                file_path = queue.pop(0)
                fruit_name, real_fruit = preform_inference(file_path)
                real_fruit = "apple"
                delta = fruit_duration_table.find_fruit_duration(real_fruit)
                msg = f"How will you store the {real_fruit}?"
                print(msg)
                # 1 for counter, 2 for pantry, 3 for fridge, 4 for freezer
                print("1. Counter")
                print("2. Pantry")
                print("3. Fridge")
                print("4. Freezer")
                storage = input("Enter a number: ")
                fruit_duration = fruit_duration_table.get_duration_values(real_fruit)[int(storage)]
                print(f"Adding {real_fruit} to inventory with expiration date of {fruit_duration} days")
                
                
                

                

    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    print("Starting fruit inventory system...")
    print("Press Ctrl+C to stop the program")
    print("Waiting for new images...")
    # Test Fruit Duration
    main()
    print("Program stopped")
    

'''

'''