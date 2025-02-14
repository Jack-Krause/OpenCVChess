import cv2
from matplotlib import pyplot as plt
import numpy as np
from Line import Line  # assuming Line is defined as a dataclass
import helper

# Opening image
img = cv2.imread("cb1.jpg")
lsd = cv2.createLineSegmentDetector(0)

# Convert image to grayscale and RGB
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detect edges and lines
lines = lsd.detect(img_gray)

if lines[0] is not None:
    # Convert the raw array into a list of Line objects
    detected_lines = [Line(*line[0]) for line in lines[0]]
    
    # Find the longest line using the length method
    longest_line = max(detected_lines, key=lambda l: l.length())
    
    print("Longest line coordinates:", longest_line)
    print("Length of the longest line:", longest_line.length())
    
    # Create a copy of the image for drawing
    drawn_img = img_rgb.copy()
    
    # Draw all lines in green
    for line in detected_lines:
        cv2.line(
            drawn_img,
            (int(line.x1), int(line.y1)),
            (int(line.x2), int(line.y2)),
            (0, 255, 0),  # green color
            1            # line thickness
        )
    
    # Draw the longest line in blue (over the green ones)
    cv2.line(
        drawn_img,
        (int(longest_line.x1), int(longest_line.y1)),
        (int(longest_line.x2), int(longest_line.y2)),
        (0, 0, 255),   # blue color
        2             # thicker line
    )
    
    # Display the result
    plt.imshow(drawn_img)
    plt.title("All Lines (green) with Longest Line Highlighted (blue)")
    plt.show()
    
    # try and find the grid
    l = helper.find_grid(detected_lines)
    if l is not None:
        print(l.length())
        cv2.line(
            drawn_img,
            (int(l.x1), int(l.y1)),
            (int(l.x2), int (l.y2)),
            (0, 0, 0),
            3
        )
        
        plt.imshow(drawn_img)
        plt.title("found line")
        plt.show()
    
    
    
else:
    print("No lines detected.")
