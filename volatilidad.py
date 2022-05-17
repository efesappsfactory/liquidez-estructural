import numpy as np
import pandas as pd

saldos_cuentas_depositos_original_df = pd.read_excel("volatilidad.xls", usecols="B:F")
scdc1_df = saldos_cuentas_depositos_original_df.iloc[0:60].reset_index(drop=True)
scdc2_df = saldos_cuentas_depositos_original_df.iloc[30:90].reset_index(drop=True)

scdr_df = np.log(scdc2_df.divide(scdc1_df)).fillna(0).std(axis=0)



print(scdr_df)
