'''
    Função Sigmoid
'''

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

numerico = np.arange(-10, 10, step=1)

fig, ax = plt.subplots(figsize=(6,4))

ax.plot(numerico, sigmoid(numerico))
plt.show()