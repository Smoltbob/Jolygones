#!/usr/bin/env python3
"""
Génère des jolygones
Paramètres : Un angle et un coefficient multiplicateur
A chaque itération, on trace une nouvelle ligne selon l'angle donné
"""

# TODO : meilleure gestion du min max : ne pas faire de seconde itération
# TODO : couleur

from math import cos, sin, pi, fabs
import svg
import argparse

def arc_en_ciel(frequence, index):
    """
    Retourne un arc-en-ceil de couleurs
    """
    rouge = sin(frequence * index + 0) * 127 + 128
    vert = sin(frequence * index + 2) * 127 + 128
    bleu = sin(frequence * index + 4) * 127 + 128
    return (rouge, vert, bleu)

def main():
    """
    Fonction principale
    """
    # Parseur d'arguments
    parser = argparse.ArgumentParser(description = "Génère des Joligones")
    parser.add_argument("-angle", "-a", help = "Angle des segments", type = float)
    parser.add_argument("-coefficient", "-c", help = "Coefficient d'atténuation", type = float)
    parser.add_argument("-iterations", "-i", help = "Nombre de segments", type = int)
    parser.add_argument("-scale", "-s", help = "Taille du jolygone", type = int)
    args = parser.parse_args()

    # Affectation des paramètres
    angle = args.angle * (pi/180)
    coeff = args.coefficient
    iterations = args.iterations
    scale = args.scale

    # Couleurs
    index = 0

    # Calcul du ymax : on itère une première fois pour trouver les extremum
    pointa = (0, 0)
    pointb = (scale, 0)
    tabx = []
    taby = []
    ligne = 1
    for _ in range(iterations):
        # Rotation du point A autour de B selon l'angle
        xc = ((pointa[0] - pointb[0]) * coeff * cos(angle)
              - (pointa[1] - pointb[1]) * coeff * sin(angle) + pointb[0])
        yc = ((pointa[0] - pointb[0]) * coeff  * sin(angle)
              + (pointa[1] - pointb[1]) * coeff * cos(angle) + pointb[1])
        pointa = pointb
        pointb = (xc, yc)
        tabx.append(pointa[0])
        taby.append(pointa[1])

    # Calcul du min et max
    maxix = max(tabx) - min(tabx)
    maxiy = max(taby) + fabs(min(taby))
    # Centrage de la figure en choisissant des
    # coordonnées de départ judicieuses
    pointa = (- min(tabx), - min(taby))
    pointb = (scale - min(tabx), - min(taby))

    (rouge, vert, bleu) = arc_en_ciel(0.03, index)
    with open("test.svg", "w+") as svg_file:
        # Ecriture de l'en-tête. On laisse de la place pour le header
        # TODO : trouver une meilleure solution ou calculer la taille
        # précise du header
        svg_file.write("                                                    ")
        svg_file.write(svg.svg_line(pointa[0], pointa[1],
                                    pointb[0], pointb[1],
                                    rouge, vert, bleu, ligne))
        for boucle in range(iterations):
            # Mise à jour des couleurs
            index += 1
            if index > 32:
                index = 0
            (rouge, vert, bleu) = arc_en_ciel(0.2, index)
            # Rotation du point A autour de B selon l'angle
            xc = ((pointa[0] - pointb[0]) * coeff * cos(angle)
                  - (pointa[1] - pointb[1]) * coeff * sin(angle) + pointb[0])
            yc = ((pointa[0] - pointb[0]) * coeff  * sin(angle)
                  + (pointa[1] - pointb[1]) * coeff * cos(angle) + pointb[1])
            # Mise à jour des points
            pointa = pointb
            pointb = (xc, yc)
            # Tracé du point
            ligne = 2/(pow(boucle + 1, 1/3))
            svg_file.write(svg.svg_line(pointa[0], pointa[1],
                                        pointb[0], pointb[1],
                                        rouge, vert, bleu, ligne))
        # Fin du fichier
        svg_file.write(svg.svg_footer())
        svg_file.seek(0)
        svg_file.write(svg.svg_header(round(maxiy, 3), round(maxix, 3)))

main()
