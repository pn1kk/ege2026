import os
import sys

sys.setrecursionlimit(5000)

def f(x):
    if x < 3:
        return 1
    if x > 2 and x % 2 == 1:
        return f(x - 1) + x
    elif x > 2 and x % 2 == 0:
        return f(x - 3) + 2 * x

print(f(2048) - f(2041))
