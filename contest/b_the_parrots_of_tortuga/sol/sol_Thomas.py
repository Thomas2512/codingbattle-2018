#!/usr/bin/env python3
import math
import numpy as np


g, n = map(int, input("# Pièces, # Dresseurs").split())
# s = np.chararray((n, 1))
s = np.empty(n, dtype="U100")
prix = np.zeros(n)
commissions = np.zeros(n)
for i in range(n):
    s[i], prix[i], commissions[i] = input("Nom, #prix unitaire, #commision").split()
prix = np.array(list(map(int, prix)))
commissions = np.array(list(map(int, commissions)))

print(s)
print(prix)
print(commissions)

nb_perroquets = np.zeros(n)
G = g * np.ones(n)
print(G)

nb_perroquets = np.floor((g - commissions) / prix)

for i in range(n):
    # nb_perroquets[i] = math.floor( (g-commissions[i]) / prix[i] )
    print(s[i], ' : ', nb_perroquets[i])
print(s[np.argmax(nb_perroquets)])
