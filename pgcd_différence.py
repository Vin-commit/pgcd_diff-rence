#!/usr/bin/python3
# coding: utf-8


# Propriétés mathématiques utilisées : 
# -----------------------------------------------
#
#        si a > b, alors pgcd(a, b) = pgcd(a-b, b)
#         si a < b, alors pgcd(a, b) = pgcd(a, b-a) 
#
# Si l’on veut ppcm(a, b) → utilisez ppcm(a, b) = a*b/pgcd(a, b). 


def pgcd_différence (a,b):
  while (a*b != 0): # ou (a*b > 0)
    if (a > b):
      a = a - b
    else:
      b = b - a
if (a == 0):
  print(“Leur pgcd est  : “,  b)
else:
  print(“Leur pgcd est  : ”,  a)


a = int(input(“Entrez le premier nombre du pgcd  :  “))
b = int(input(“Entrez le second nombre du pgcd  :  “))
pgcd_différence (a, b)


----------------------------------------------------------------------- Résultat --------------------------------------------------------------------------
 scrot.png