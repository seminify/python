import pandas as pd

df = pd.read_excel('Sample.xlsx')
row = [{'name': 'Lim', 'age': 64, 'city': 'Jeju', 'children': 2, 'pets': 1}]
df = df.append(row, 'sort=False')
writer = pd.ExcelWriter('Sample.xlsx', engine='openpyxl')
df.to_excel(writer, index=False)
writer.save()
