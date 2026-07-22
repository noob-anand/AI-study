import matplotlib.pyplot as plt
import numpy as np

x=np.array([2023,2024,2025,2026])
y=np.array([15,25,30,20])


plt.plot(x,y,
         marker=".",
         markersize=10,
         markerfacecolor="red",
         markeredgecolor="red",
         linestyle="dashed",
         linewidth=2,
         color="green")


plt.show()