#!/usr/bin/env python3
import math


L, N = map(int, input().split())

def riddle(n):
    digits = '0123456789'
    result = ''
    for digit in digits:
        compte = str(n).count(str(digit))
        print(compte)
        if compte >= 1:
            result = result + str(compte) + str(digit)
    return result

# while(True):
#     a = input()
#     print(riddle(a))

def riddle_mutliple(n,p):
    if p == 1:
        return riddle(n)
    else:
        return riddle( riddle_mutliple(n, p-1) )

print( riddle_mutliple(L, N) )