'''
    Hipótese - Rede Multicamadas
'''

import numpy as np
import matplotlib.pyplot as plt

w0 = 0.3
w1 = 0.3

def hipotese(x, w0, w1):
    return w0 + w1 * x

hipotese(1, w0, w1)


x = np.arange(-10, 10, step=1)

h = hipotese(x, w0, w1)

lenh = np.arange(0, 20)

pontosY = [4, 5, 5]
pontosX = [5, 3, 4]

plt.scatter(pontosY, pontosX)
plt.title(' Redes Multicamadas - Hipótese')
plt.grid(True)
plt.plot(lenh, h)
plt.show()