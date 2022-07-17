import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('Sample.xlsx')
df['age'].plot(kind='hist', bins=[0, 20, 40, 60, 80, 100], rwidth=0.8)
plt.show()
