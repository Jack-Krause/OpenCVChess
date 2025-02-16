from Line import Line  # assuming Line is defined as a dataclass
import helper
import os

directory = "images"
files = []
n = 0

for f in os.listdir(directory):
    n += 1
    if os.path.isfile(os.path.join(directory, f)) and f.endswith(".jpg") or f.endswith(".webp"):
        helper.open_file(os.path.join(directory, f), n)
