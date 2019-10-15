#!/usr/bin/env python3
import math
while(True):
    P, L, G = map(int, input().split())
    count = 0
    for x in range(min(P, math.ceil(math.sqrt(G)))):
        for y in range(L):
            result = x**2 + y + x * y
            count += (result==G)
    print(count)
