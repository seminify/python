import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('Sample.xlsx')
df.plot(kind='bar', x='name', y='age')
plt.show()
