'''
    Função Delta
'''
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivadaParcial(sig):
    return sig * (1 - sig)

def deltaSaida(erro, dev):
    return erro * dev

def deltaDaEscondida(derivadaParcial, peso, deltaSaida):
    return derivadaParcial * peso * deltaSaida


erro = 0.5

dev = derivadaParcial(0.5)
ds = deltaSaida(erro, dev)
peso = 0.2

dtEscondido = deltaDaEscondida(dev, peso, ds)

print(dtEscondido)