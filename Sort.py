import shutil
import pandas as pd
import xlrd

a = pd.read_excel("sample.xlsx")



a =a.sort_values('name')

a.to_csv("sampe_out.csv", index=False)

#b = pd.read_csv("pcontact.csv")

#merged = pd.merge(a, b, how='inner', on=['CONTACT_ID', 'CONTACT_ID'])
#merged.to_csv("output.csv", index=False)

