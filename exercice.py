#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def calcul_volume_et_masse (axe_a, axe_b, axe_c, masse_volumique) :
    Volume = 4/3 * math.pi *axe_a * axe_b * axe_c
    Masse = masse_volumique * Volume
    return (Volume, Masse)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    données = input("Veuillez entre vos trois demis-ax")
    pass
