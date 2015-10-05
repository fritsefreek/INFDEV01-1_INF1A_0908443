﻿size = int(raw_input("Size: "))
scale = size / 10
figure = ""

for i in range(0, size):
    for x in range(0, size):
        # Border
        if (i == (0 * scale) or i == (8 * scale)) and (x == (3 * scale) or x == (4 * scale) or x == (5 * scale)):
            figure += "*"
        elif (i == (1 * scale) or i == (7 * scale)) and (x == (2 * scale) or x == (6 * scale)):
            figure += "*"
        elif (i == (2 * scale) or i == (6 * scale)) and (x == (1 * scale) or x == (7 * scale)):
            figure += "*"
        elif (i == (3 * scale) or i == (4 * scale) or i == (5 * scale)) and (x == (0 * scale) or x == (8 * scale)):
            figure += "*"
        # Eyebrows
        elif i == (2 * scale) and (x == (2 * scale) or x == (6 * scale)):
            figure += "-"
        # Eyes
        elif i == (3 * scale) and (x == (2 * scale) or x == (6 * scale)):
            figure += "o"
        # Nose
        elif i == (5 * scale) and x == (4 * scale):
            figure += "#"
        # Cheek left
        elif i == (5 * scale) and x == (2 * scale):
            figure += "\\"
        # Cheek right
        elif i == (5 * scale) and x == (6 * scale):
            figure += "/"
        # Mouth
        elif i == (6 * scale) and (x == (3 * scale) or x == (4 * scale) or x == (5 * scale)):
            figure += "-"
        else:
            figure += " "

    figure += "\n"

print(figure)