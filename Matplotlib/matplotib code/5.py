import matplotlib.pyplot as plt
import numpy as np

# Bar Chart of image data

categories=np.array(["Grains","Fruits","Vegitables","Protein","Dairy","Sweets"])
values=np.array([4,3,2,5,3,1])

plt.bar(categories,values,color="Green") #for verticle
# plt.barh(categories,values,color="Green") #for horizontal

plt.title("Daily consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()