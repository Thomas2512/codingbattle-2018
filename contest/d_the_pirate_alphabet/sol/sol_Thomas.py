#!/usr/bin/env python3
import math
import numpy as np
import string

s = input()

alphabet_pirate = 'aeiouybcdfghjklmnpqrstvwxz'
alphabet = string.ascii_lowercase

# On crée la correspondance entre les 2 alphabets
dict = {}
for i in range(len(alphabet_pirate)):
    dict[alphabet_pirate[i]] = i

def pirate2normal(s):
    list_index=[]
    list_char=[]
    for i in range(len(s)):
        list_index.append(dict[s[i]])
        list_char.append(alphabet[dict[s[i]]])
    return ''.join(list_char)



# On fait d'abord le problème sur le vrai alphabet plutôt que sur l'alphabet pirate

def compte_desordres(test):
    n = len(test)

    list = np.zeros(n)

    for i in range(n):
        count = 0
        for j in range(n):
            if i < j:
                count += (test[i] > test[j])
            if i > j:
                count += (test[i] < test[j])

            # print(i, j, test[i], test[j], ' : ', count)
        list[i] = int(count)
        print(test[i], ' : ', list[i])

    return list

# while compte_desordres(s).sum() != 0:
#     print('1 ', s)
#     index_to_remove = np.argmax(compte_desordres(s))
#     s = s[:index_to_remove] + s[index_to_remove+1:]
#     print('2 ', s)

def filtre_doublons(s):
    s_new = ''
    for i in range(len(s)):
        letter = s[i]
        if letter not in s_new:
            s_new += letter
    return s_new


def to_insert_number(s):
    s = filtre_doublons(s)
    while compte_desordres(s).sum() != 0:
        print('1 ', s)
        index_to_remove = np.argmax(compte_desordres(s))
        s = s[:index_to_remove] + s[index_to_remove + 1:]
        print('2 ', s)
    return 26 - len(set(s))

print(to_insert_number( pirate2normal(s) ))