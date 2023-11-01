import Pacific
import math
import random

def f1(x, y):
    return x+math.cos(y)

def f2(x, y):
    return x*math.sin(y)

def f1p(x, y):
    return x+math.cos(y)

def f2p(x, y):
    return x*math.sin(y)

Pacific.generate(f1, f2, .5, '#7de2d1', f1p, f2p, .5, '#ff3d33', .5, '#f68b08', .5, '#2cdddd', random.randint(-100, 100), random.randint(100, 200), random.randint(-100, 100), random.randint(100, 200), True)
