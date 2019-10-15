#!/usr/bin/env python3
import math
import numpy as np


l, n = map(int, input("Longueur, # Pirates").split())
postes = [int(x) for x in input("Positions des postes de combat").split()]
chapeaux =  [int(x) for x in input("Tailles des chapeaux").split()]


def possible(l, n, postes, chapeaux):
    if len(chapeaux) == 1:

