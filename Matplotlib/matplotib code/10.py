import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# matplotlib with pandas

a=pd.read_csv("E:\code\AI study\Matplotlib\matplotib code\data.csv")

cnt= a["Type1"].value_counts(ascending=True)

plt.barh(cnt.index, cnt.values,
        color="teal")

plt.show()
