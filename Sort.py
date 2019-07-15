import shutil
import pandas as pd
import xlrd

a = pd.read_excel("sample.xlsx")


s = a.Col1.str.len().sort_values(ascending=False).index
#print(a.Col1.str.len().sort_values(ascending=False))
#print(s)
df1 = a.reindex(s)
df1 = df1.reset_index(drop=True)
#print(df1)
#a =a.sort_values(by=['Col1'])



#print(a.Col1.str.len().sort_values(ascending=False))

df1.to_csv("sampe_out.csv",index=False)

#b = pd.read_csv("pcontact.csv")

#merged = pd.merge(a, b, how='inner', on=['CONTACT_ID', 'CONTACT_ID'])
#merged.to_csv("output.csv", index=False)

