import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([5,11,17,23,29])

plt.grid(linestyle="dotted")

plt.plot(x,y)

plt.show()