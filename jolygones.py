#!/usr/bin/env python3
"""
Generates Jolygones.
To make one we start wih a line segment. Each new segment is obtained
from the last one, by adding a rotation. (see examples)
Parameters : an angle and a coefficient
At each iteration, we trace a new line according to the given angle.
"""

# TODO : random angles
# TODO : no preprocessing
# TODO : use functions
# TODO : handle error when there is no arguments
# TODO : handle missing arguments
# TODO : use a single tab

from math import cos, sin, pi, fabs
import svg
import argparse

def rainbow(frequence, index):
    """
    Returns the RGB values to make a rainbow
    """
    rouge = sin(frequence * index + 0) * 127 + 128
    vert = sin(frequence * index + 2) * 127 + 128
    bleu = sin(frequence * index + 4) * 127 + 128
    return (rouge, vert, bleu)

def main():
    """
    Main loop.
    Handles arguments and computes the Jolygone
    """
    # Parsing arguments
    parser = argparse.ArgumentParser(description = "Generates Jolygones")
    parser.add_argument("-angle", "-a", help = "Angle of segments rotation", type = float)
    parser.add_argument("-coefficient", "-c", help = "Coefficient of attenuation", type = float)
    parser.add_argument("-iterations", "-i", help = "Number of segments", type = int)
    parser.add_argument("-scale", "-s", help = "Size of Jolygone", type = int)
    args = parser.parse_args()

    # Affecting parameters
    angle = args.angle * (pi/180)
    coeff = args.coefficient
    iterations = args.iterations
    scale = args.scale

    # Colors
    index = 0

    # Computing ymax : we iterate a first time to find extremums.
    # It is better to compute the extremums directly with a formula.
    # We will use arrays to store the Jolygone points
    pointa = (0, 0)
    pointb = (scale, 0)
    tabx = []
    taby = []
    ligne = 1
    for _ in range(iterations):
        # Rotation of point A around point B according to the angle.
        xc = ((pointa[0] - pointb[0]) * coeff * cos(angle)
              - (pointa[1] - pointb[1]) * coeff * sin(angle) + pointb[0])
        yc = ((pointa[0] - pointb[0]) * coeff  * sin(angle)
              + (pointa[1] - pointb[1]) * coeff * cos(angle) + pointb[1])
        pointa = pointb
        pointb = (xc, yc)
        tabx.append(pointa[0])
        taby.append(pointa[1])

    # Computing the span of the figure
    maxix = max(tabx) - min(tabx)
    maxiy = max(taby) + fabs(min(taby))

    # Centering the figure by using appropriate coordinates
    pointa = (- min(tabx), - min(taby))
    pointb = (scale - min(tabx), - min(taby))

    (rouge, vert, bleu) = rainbow(0.03, index)

    # Generating figure
    with open("test.svg", "w+") as svg_file:
        # We keep some room for the header
        #svg_file.write("                                                    ")
        svg_file.write(svg.svg_header(round(maxiy, 3), round(maxix, 3)))
        svg_file.write(svg.svg_line(pointa[0], pointa[1],
                                    pointb[0], pointb[1],
                                    rouge, vert, bleu, ligne))
        for boucle in range(iterations):
            # Updating colors
            index += 1
            if index > 32:
                index = 0
            (rouge, vert, bleu) = rainbow(0.2, index)
            # Rotating point A around point B according to the angle
            xc = ((pointa[0] - pointb[0]) * coeff * cos(angle)
                  - (pointa[1] - pointb[1]) * coeff * sin(angle) + pointb[0])
            yc = ((pointa[0] - pointb[0]) * coeff  * sin(angle)
                  + (pointa[1] - pointb[1]) * coeff * cos(angle) + pointb[1])
            # Updating points
            pointa = pointb
            pointb = (xc, yc)
            # Tracing line
            ligne = 2/(pow(boucle + 1, 1/3))
            svg_file.write(svg.svg_line(pointa[0], pointa[1],
                                        pointb[0], pointb[1],
                                        rouge, vert, bleu, ligne))
        # End of figure
        svg_file.write(svg.svg_footer())

# Calling script only if lauched (not imported)
if __name__ == '__main__':
    main()
