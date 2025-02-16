from Line import Line  # assuming Line is defined as a dataclass
import helper
import os
import cv2

directory = "images"
n = 0

for f in os.listdir(directory):
    file_path = os.path.join(directory, f)

    if os.path.isfile(file_path) and f.endswith(".jpg") or f.endswith(".webp"):
        n += 1
        img = cv2.imread(file_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        width, height, _ = img.shape

        # helper.find_lines_plot(img_gray, img_rgb, n)

        helper.find_square(img_rgb, width, height)
