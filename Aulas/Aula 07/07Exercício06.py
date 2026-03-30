from math import *


def calcmaldito (x, y, z):
    k = sqrt(x) + sqrt(y) + sqrt(z) + (x + y)/2 + (y+z)/2 + (x+z)/2
    print (k)

calcmaldito (3, 2 ,1)