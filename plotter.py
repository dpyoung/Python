#!/usr/bin/python

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("custom_data.csv")

sns.scatterplot(x='Product', y='Total Sales',
                hue='Country', data=df, )

plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()
