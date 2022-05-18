import numpy as np
import pandas as pd

saldos_depositos_df = pd.read_excel("volatilidad.xls", usecols = "B:F")

saldos_depositos_1 = saldos_depositos_df.iloc[0:60].reset_index(drop=True)
saldos_depositos_2 = saldos_depositos_df.iloc[30:90].reset_index(drop=True)

saldos_normalizados = np.log(saldos_depositos_2.divide(saldos_depositos_1)).fillna(0)

var_s = saldos_normalizados.std(axis=0).multiply(saldos_depositos_df.iloc[89])

corr_matrix = saldos_normalizados.corr().fillna(0)

var_total = np.sqrt(var_s.dot(var_s.transpose().dot(corr_matrix)))

total_depositos_last_day = saldos_depositos_df.iloc[89].agg('sum')

volatilidad_general = var_total/total_depositos_last_day

print(volatilidad_general)
