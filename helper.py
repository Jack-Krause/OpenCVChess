# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:47:53 2025

@author: jackm
"""
from Line import Line
import cv2
from matplotlib import pyplot as plt
from matplotlib import patches as patches
from Line import Line


def find_lines_plot(img_gray, img_rgb, n):
    lsd = cv2.createLineSegmentDetector(0)
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
                1  # line thickness
            )

        # Draw the longest line in blue (over the green ones)
        cv2.line(
            drawn_img,
            (int(longest_line.x1), int(longest_line.y1)),
            (int(longest_line.x2), int(longest_line.y2)),
            (0, 0, 255),  # blue color
            2  # thicker line
        )

        # Display the result
        plt.imsave("plots/longest_lines/fig_longest_line" + str(n) + ".png", drawn_img)
        plt.imshow(drawn_img)
        plt.title("All Lines (green) with Longest Line Highlighted (blue)")
        plt.show()

        # try and find the grid
        l = find_small_line(detected_lines)
        if l is not None:
            print(l.length())
            cv2.line(
                drawn_img,
                (int(l.x1), int(l.y1)),
                (int(l.x2), int(l.y2)),
                (255, 0, 0),
                3
            )

            plt.imsave("plots/finding_lines/line_found" + str(n) + ".png", drawn_img)
            plt.imshow(drawn_img)
            plt.title("found line in red")
            plt.show()

    else:
        print("No lines detected.")


def find_grid(line, x1_approx, y1_approx, x2_approx, y2_approx):
    l = line.length()
    for candidate in line:
        if (x1_approx - 10) <= candidate.x1 <= (x1_approx + 10):
            print()


def find_small_line(lines):
    if lines[0] is not None:
        for line in lines:
            if line.length() > 10 and line.length() < 100:
                return line


def find_square(img_rgb, width, height):
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    rows, cols = 4, 4
    r_width = width / cols
    r_height = height / rows
    partition = 1

    for i in range(rows):
        for j in range(cols):
            x0 = round(j * r_width, 2)
            y0 = round(i * r_height, 2)

            print("***** Partition", partition)
            print("(x, width):", f"({x0}, {r_width})")
            print("(y, height):", f"({y0}, {r_height})")
            print()

            rect = patches.Rectangle(
                (x0, y0), r_width, r_height,
                linewidth=2, edgecolor=f"C{partition % 10}",
                facecolor='none', label=f'Partition {partition}'
            )
            ax.add_patch(rect)

            # Label the partition at its center
            center_x = x0 + r_width / 2
            center_y = y0 + r_height / 2
            ax.text(center_x, center_y, str(partition),
                    color='black', fontsize=12,
                    ha='center', va='center')

            partition += 1

    ax.set_aspect('equal', adjustable='box')
    ax.set_title("16 Partitions of the x, y Plane")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Show the plot
    plt.show()
    plt.close(fig)
