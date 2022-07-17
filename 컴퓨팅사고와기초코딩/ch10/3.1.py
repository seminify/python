import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('Sample.xlsx')
df.plot(kind='line', x='name', y='pets', color='red')
plt.show()
