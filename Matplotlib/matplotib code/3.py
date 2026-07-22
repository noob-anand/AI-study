import matplotlib.pyplot as plt
import numpy as np

x=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y2=np.array([13,50,45,65])
y3=np.array([10,15,50,10])

plt.title("Class size",
          fontsize=25,
          family="Arial",
          fontweight="bold",
          color="#3d39a9ff")

style=dict(fontsize=15,
           family="Arial",
           fontweight="bold"
            )

plt.xlabel("Year",**style)

plt.ylabel("Students",**style)

plt.tick_params(axis="both",
                color="cyan")

plt.xticks(x)

plt.plot(x, y1,color="blue")
plt.plot(x, y2,color="green")
plt.plot(x, y3,color="red")

plt.show()