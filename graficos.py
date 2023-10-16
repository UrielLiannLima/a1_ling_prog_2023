import matplotlib.pyplot as plt
import numpy as np
import limpar_df as ldf
import pandas as pd

# NO_REGIAO
# IN_AGUA_INEXISTENTE
# IN_ENERGIA_INEXISTENTE
# IN_ESGOTO_INEXISTENTE
# IN_LIXO_SERVICO_COLETA
# IN_BANHEIRO
# IN_BIBLIOTECA
# IN_LABORATORIO_INFORMATICA
# IN_QUADRA_ESPORTES
# IN_SALA_DIRETORIA
# IN_SALA_PROFESSOR
# IN_SECRETARIA
# IN_ACESSIBILIDADE_INEXISTENTE
# IN_ALIMENTACAO
# IN_MATERIAL_PED_NENHUM

# Abrir o arquivo de dados e estruturação
df = ldf.open_df("data.csv")
structure_df = ldf.remove_outliers(ldf.drop_cols("indexes/custom.txt", ldf.drop_cols("indexes/base.txt", df)))

# Busca os dados únicos na coluna
regioes = structure_df["NO_REGIAO"].unique()

# Suponhamos que sua base de dados tenha uma coluna chamada 'texto' que você deseja analisar
coluna_desejada = 'NO_REGIAO'

# Se você quiser contar uma palavra específica, por exemplo, 'exemplo', você pode fazer o seguinte:
palavra_alvo = 'Norte'

# Use o método str.count() para contar o número de ocorrências da palavra na coluna
contagem_palavra_alvo = dados[coluna_desejada].str.lower().str.count(palavra_alvo.lower()).sum()

print(f"A palavra '{palavra_alvo}' aparece {contagem_palavra_alvo} vezes na coluna.")



