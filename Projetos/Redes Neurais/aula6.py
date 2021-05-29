'''
    Função Sigmoid
'''
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivadaParcial(sig):
    return sig * (1 - sig)


x = np.array([1, 2, 3, 4, 5])

dev = derivadaParcial(sigmoid(x))

print(dev)

plt.plot(x,dev)
plt.show()