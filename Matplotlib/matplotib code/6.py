import matplotlib.pyplot as plt
import numpy as np

# Pie Chart of image data

categories=np.array(["Freshmen","Sophomores","Juniors","Seniors"])
values=np.array([300,250,275,225])

colors=np.array(["red","yellow","blue","green"])

plt.pie(values,
        labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0,0,0,0.1],
        shadow=True,
        startangle=180
        )

plt.title("Bro Code College")

plt.show()