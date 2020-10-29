#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
#sys.path.insert(1, "file")
#from c04_ch6_exercices.exercice import frequence
from turtle import *


# TODO: Définissez vos fonction ici
def calcul_volume_et_masse(axe_a=2, axe_b=4, axe_c=2, masse_volumique=10):
    Volume = 4 / 3 * math.pi * axe_a * axe_b * axe_c
    Masse = masse_volumique * Volume
    return (Volume, Masse)


def draw_tree():
    setheading(90)
    color("green")
    draw_branch()
    done()

def draw_branch(branch_len=70, pen_size=7, angle=35):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)


def profondeur_liste(liste, profondeur=0, liste_de_profondeur=[]):
    if type(liste) is not list:
        return profondeur

    for elem in liste:
        liste_de_profondeur.append(profondeur_liste(elem, profondeur + 1, liste_de_profondeur))

    return max(liste_de_profondeur)





if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(calcul_volume_et_masse(axe_a=7))
    # (lambda sentence: sorted(frequence(sentence), key=))
    # print(frequence("phrase"))
    #draw_tree()
    print(profondeur_liste([1, 2, [3, 4]]))
    pass
