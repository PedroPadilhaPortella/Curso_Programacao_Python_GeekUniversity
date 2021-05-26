'''
    Hipótese
'''

import numpy as np
import matplotlib.pyplot as plt

w0 = 0.3
w1 = 0.3

def hipotese(x, w0, w1):
    return w0 + w1 * x

print(hipotese(2, w0, w1))