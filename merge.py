import pandas as pd

a = pd.read_csv("pwinners.csv")
b = pd.read_csv("pcontact.csv")

merged = pd.merge(a, b, how='inner', on=['CONTACT_ID', 'CONTACT_ID'])
merged.to_csv("output.csv", index=False)