import pandas as pd
import os


p="/storage/emulated/0"
f="1/mytools/2st.xlsx"

fp=os.path.join(p, f)

df=pd.read_excel(fp)
print(df)