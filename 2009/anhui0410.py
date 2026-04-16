import pandas as pd
file=r"F:\tbc0410\GDPxy\2009\1 县(市)社会经济主要指标\安徽省.xlsx"
df = pd.read_excel(file,engine='openpyxl')

df.info()
df.head()

df.isnull().sum()
df.unique
