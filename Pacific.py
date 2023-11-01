import math
import matplotlib.pyplot as plt

def signum(x):
    if x > 0:   return 1
    if x < 0:   return -1
    return 0

def generate(f1, f2, s1, c1, f1p, f2p, s2, c2, s3, c3, s4, c4, a=-100, b=101, c=-100, d=101, dark=False):
    if dark:    plt.style.use('dark_background')
    try:
        plt.axis('off')
        S1 = [(f1(i, j), f2(i, j)) for i in range(a, b) for j in range(c, d)]
        x1, y1 = zip(*S1)
        plt.scatter(x1, y1, s=s1, c=c1)
        plt.show()
    except:
        print('Input Error')
    try:
        plt.axis('off')
        S2 = [(f1p(i, j), f2p(i, j)) for i, j in zip(x1, y1)]
        x2, y2 = zip(*S2)
        plt.scatter(x2, y2, s=s2, c=c2)
        plt.show()
    except:
        print('Output Error')
    try:
        polar = [(math.sqrt(i**2+j**2), math.atan(j/i)) for i, j in zip(x2, y2) if i != 0]
        xp, yp = zip(*polar)
        ax = plt.figure().add_subplot(projection='polar')
        ax.axis('off')
        ax.scatter(yp, xp, s=s3, c=c3)
        plt.show()
    except:
        print('Polar Error')
    try:
        parabolic = [(signum(i)*math.sqrt(math.sqrt(i**2+j**2)-j), math.sqrt(math.sqrt(i**2+j**2)+j)) for i, j in zip(x2, y2)]
        xp2, yp2 = zip(*parabolic)
        plt.scatter(xp2, yp2, s=s4, c=c4)
        plt.axis('off')
        plt.show()
    except:
        print('Parabolic Error')
