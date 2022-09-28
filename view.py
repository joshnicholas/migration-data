# %%
import pandas as pd 
# pd.set_option("display.max_rows", 100)

fillo = 'input/out/20220928.csv'
#%%

data = pd.read_csv(fillo)

#%%

df = data.copy()

p = df

# vchecker = 'gdp_per_capita'
# print(p.loc[p[vchecker].isna()])
print(p)
print(p.columns.tolist())