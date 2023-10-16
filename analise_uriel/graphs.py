import sys
import os
import pandas as pd
import matplotlib

# Permite puxar do módulo 1 diretório acima para importar o limpar_df
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import limpar_df as ldf

# Abre o diretório e remove as colunas não utilizadas como também as linhas com outliers
df = ldf.open_df("../data.csv")
working_df = ldf.remove_outliers(ldf.drop_cols("not_used.txt", df))

working_df.to_csv("working.csv", index=False)