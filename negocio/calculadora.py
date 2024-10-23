import math

def calcular(a, b):
    if (a <= 0 or b <= 0):
        return 0
    return math.floor(a/b)