import matplotlib.pyplot as plt
import numpy as np

# Subplot

# print(plt.subplots(2,2))

x=np.array([1,2,3,4,5])

fig, ax = plt.subplots(2, 2)

#1
ax[0,0].plot(x, x,
             color="red")
ax[0,0].set_title("y=x")

#2
ax[0,1].plot(x, x**2,
             color="blue")
ax[0,1].set_title("y=x^2")

#3
ax[1,0].plot(x, x**3,
             color="green")
ax[1,0].set_title("y=x^3")

#4
ax[1,1].bar(x, x**4,
             color="orange")
ax[1,1].set_title("y=x^4")


plt.tight_layout()

plt.show()

