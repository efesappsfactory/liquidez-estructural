import numpy as np
import pandas as pd

saldos_depositos_df = pd.read_excel("volatilidad.xls", usecols = "B:F")

def calcular_volatilidad_general(saldos_df):
  saldos_1 = saldos_df.iloc[0:60].reset_index(drop=True)
  saldos_2 = saldos_df.iloc[30:90].reset_index(drop=True)

  saldos_normalizados = np.log(saldos_2.divide(saldos_1)).fillna(0)

  corr_matrix = saldos_normalizados.corr().fillna(0)

  var_s = saldos_normalizados.std(axis=0).multiply(saldos_df.iloc[89])

  var_total = np.sqrt(var_s.dot(var_s.transpose().dot(corr_matrix)))

  total_depositos_last_week = saldos_df.iloc[85:90].agg('sum', axis=1)

  volatilidad_per_day = var_total/total_depositos_last_week

  total_depositos_last_day = saldos_df.iloc[89].agg('sum')

  volatilidad_general = var_total/total_depositos_last_day

  return volatilidad_per_day


print(calcular_volatilidad_general(saldos_depositos_df))
