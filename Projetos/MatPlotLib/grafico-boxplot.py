'''
    BoxPlot
'''
import random
import matplotlib.pyplot as plt

vetor = []

for i in range(0, 20):
    vetor.append(random.randint(0, 10))

plt.title('BoxPlot')
plt.boxplot(vetor)
plt.show()