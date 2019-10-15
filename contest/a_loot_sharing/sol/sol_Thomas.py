#!/usr/bin/env python3
import math


b, t, n = map(int, input("#Bicornes, # Tricornes, #Pièces").split())

to_distribute = 2*b + 3*t
if to_distribute <= n:
    result = 'Loot!'
else:
    result = 'Rhum!'
print(result)