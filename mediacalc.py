# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YCi0S5SmKzuHnMVxBfmpURe4pVbaQMWF
"""

def avgcalc(a):
  if (a <= 100 ) and ( a >= 0):
    if (a >= 90) and (a <= 100):
      return("Nota final:", a,"Média A!");
    if (a >= 70 ) and (a < 90):
      return("Nota final:", a,"Média B!");
    if (a >= 50 ) and (a < 70):
      return("Nota final:", a,"Média C!");
    else:
      return("Nota final: ", a,"Média D!");
  else:
    return("Nota final:", a,"Nulo!")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))
nota3 = float(input("Digite a primeira nota: "))

avg=(nota1+nota2+nota3)/3

avgcalc(avg)

