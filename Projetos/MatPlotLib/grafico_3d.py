import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import get_test_data
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = get_test_data(0.01)

graf = ax.plot_wireframe(x, y, z)
plt.show()