import matplotlib.pyplot as plt
import numpy as np

# Histograms of image data

score=np.random.normal(loc=80,scale=10,size=100)
score=np.clip(score,0,100)

plt.hist(score,
         bins=10,
         color="lightgreen",
         edgecolor="green"
         )


plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("No of student")

plt.show()