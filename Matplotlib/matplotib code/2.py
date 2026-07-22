import matplotlib.pyplot as plt
import numpy as np

x=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y2=np.array([14,50,42,65])
y3=np.array([13,15,50,10])

style=dict(marker=".",
            markersize=10,
            markerfacecolor="red",
            markeredgecolor="red",
            linestyle="dashed",
            linewidth=2,
            )

plt.plot(x, y1,color="blue", **style)

plt.plot(x, y2,color="green", **style)

plt.plot(x, y3,color="purple", **style)

plt.show()