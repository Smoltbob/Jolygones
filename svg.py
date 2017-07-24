#!/usr/bin/env python3
"""
Module svg
"""


def svg_header(haut, larg):
    """
    Genere la premiere ligne du fichier svg
    """
    head = "<svg width=\"{}\" height=\"{}\">".format(larg, haut)
    return head

def svg_footer():
    """
    Genere la derniere ligne du fichier svg
    """
    return "</svg>"

def svg_line(coord_x1, coord_y1, coord_x2, coord_y2, rouge, vert, bleu, ligne):
    """
    Genere une ligne a partir des coordonnees de deux points
    """
    line = "<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" style=\"stroke:rgb({},{},{});stroke-width:{}\" />".format(
        coord_x1,
        coord_y1,
        coord_x2,
        coord_y2,
        rouge,
        vert,
        bleu,
        ligne)
    return line
