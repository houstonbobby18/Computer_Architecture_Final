import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

import fruit_duration
import fruit_inventory
import inferencing

def update_databases(file_path):
    print("Running inference...")
    start_time = time.time()
    fruit_name = inferencing.run_model(file_path)
    print(f"Inference took {time.time() - start_time} seconds")
    print(f"Detected fruit: {fruit_name}")
    # if input is not y ask for real fruit name
    real_fruit = input("Is the detected fruit correct? (y/n): ")
    if real_fruit == 'n':
        real_fruit = input("What is the real fruit name?: ")
    fruit_inventory
    exp_fruit_date = fruit_duration.Fruit('apple')
    exp_fruit_date = exp_fruit_date.counter_storage
    fruit_inventory.connect()
    fruit_inventory.add_item(file_path, exp_fruit_date, fruit_name, real_fruit)
    print("Item added to inventory")


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
    observer.schedule(event_handler, "./images_processed", recursive=False)
    observer.start()
    queue = []
    try:
        while True:
            queue.extend(event_handler.queue)
            event_handler.queue.clear()
            time.sleep(1)
            if len(queue) > 0:
                file_path = queue.pop(0)
                update_databases(file_path)
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