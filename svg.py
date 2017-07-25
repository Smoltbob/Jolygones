#!/usr/bin/env python3
"""
SVG functions
"""


def svg_header(height, width):
    """
    Generates the first line of svg files
    """
    head = "<svg width=\"{}\" height=\"{}\">".format(width, height)
    return head

def svg_footer():
    """
    Genere la derniere ligne du fichier svg
    """
    return "</svg>"

def svg_line(coord_x1, coord_y1, coord_x2, coord_y2, red, green, blue, thickness):
    """
    Generates a line from the coordinates of two points
    """
    line = "<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" style=\"stroke:rgb({},{},{});stroke-width:{}\" />".format(
        coord_x1,
        coord_y1,
        coord_x2,
        coord_y2,
        red,
        green,
        blue,
        thickness)
    return line
