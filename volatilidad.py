import numpy as np
import pandas as pd

saldos_depositos_df = pd.read_excel("volatilidad.xls", usecols = "B:F")

saldos_depositos_1 = saldos_depositos_df.iloc[0:60].reset_index(drop=True)
saldos_depositos_2 = saldos_depositos_df.iloc[30:90].reset_index(drop=True)

var_s = np.log(saldos_depositos_2.divide(saldos_depositos_1)).fillna(0).std(axis=0)

print(var_s)
