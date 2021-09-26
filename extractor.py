#Importing Libraries
import camelot as cm

input_pdf = cm.read_pdf('india_factsheet_economic_n_hdi.pdf',flavor='lattice',pages='1,2')

#for n in input_pdf:
    # print(n)

df=input_pdf[2].df.loc[11:14,1:3]

df = df.reset_index(drop=True)
df.columns = ["KPI","2001","2011"]

df.loc[:,["2001","2011"]] = df.loc[:,["2001","2011"]].astype(float)
# df.to_csv('table_from_pdf.csv')
# df.to_excel('table_from_pdf.xlsx')

import pandas as pd
df2 = pd.read_csv('table_from_pdf.csv')

import seaborn as sns
df_melted = df.melt('KPI', var_name='year', value_name='percentage')

sns.barplot(x = "KPI", y = "percentage", hue = "year", data = df_melted)

#Ghostwriter needed to perform operations.