import os
import shutil

temp_path = r"C:\Windows\Temp"

# Loop through all items in the temp folder
for item in os.listdir(temp_path):
    item_path = os.path.join(temp_path, item)  # Full path of the item
    try:
        # If item is a file or a symbolic link, delete it
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        # If item is a folder, delete the entire folder and its contents
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    except Exception:
        # Skip files/folders that are in use or cannot be deleted
        print("Exception for " + item_path)
        pass