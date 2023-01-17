import os

source_dir = "/home/diego/Downloads"


with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)
