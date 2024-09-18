import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from inferencing import run_model


class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None:
        if event.event_type == "created":
            print(f"Event type: {event.event_type}  path : {event.src_path}")
            time.sleep(1)
            fruit = run_model(event.src_path)
            print(f"Predicted fruit is: {fruit}")


event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, "./new_files", recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()