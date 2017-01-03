import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('firstdata.csv')


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# making a histogram
ax.hist(df['Age'],bins = 10)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Employee')
plt.show()

#boxplot
ax.boxplot(df['Age'])
plt.show()

#violin plot
sns.violinplot(df['Age'],df['Gender'])
sns.despine()
