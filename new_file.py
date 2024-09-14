import os
import time

def detect_new_files(folder_path):
    # Get the list of files in the folder
    files = set(os.listdir(folder_path))
    # Filter out only the files with .jpg extension
    while True:
        new_files = set(filter(lambda x: x.endswith(".jpg"), os.listdir(folder_path)))
        # Get the new files
        new_files = new_files - files
        if new_files:
            return new_files
        time.sleep(1)

if __name__ == "__main__":
    new_files = detect_new_files("new_files")
    print(new_files)