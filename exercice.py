#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
#sys.path.insert(1, "file")
#from c04_ch6_exercices.exercice import frequence

# TODO: Définissez vos fonction ici
def calcul_volume_et_masse (axe_a=2, axe_b=4, axe_c=2, masse_volumique=10) :
    Volume = 4/3 * math.pi *axe_a * axe_b * axe_c
    Masse = masse_volumique * Volume
    return (Volume, Masse)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(calcul_volume_et_masse(axe_a=7))
    #print()
    pass
