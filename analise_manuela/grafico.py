import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("oferta_matriculas.csv", sep=",")

df_agrupado = df.groupby("NO_REGIAO").sum()

colunas_raca = ["QT_MAT_BAS_ND", "QT_MAT_BAS_BRANCA", "QT_MAT_BAS_PRETA", "QT_MAT_BAS_PARDA", "QT_MAT_BAS_AMARELA", "QT_MAT_BAS_INDIGENA"]

dados_filtrados = df_agrupado[colunas_raca]

dados_porcentagem = dados_filtrados.div(dados_filtrados.sum(axis=1), axis=0) * 100

dados_porcentagem["NO_REGIAO"] = df_agrupado.index

rotulos_raca = ["Não declarada", "Branca", "Preta", "Parda", "Amarela", "Indígena"]

print("Distribuição de Cor/Raça por Região:")
for index, row in dados_porcentagem.iterrows():
    print(f"Região {index}:")
    for i, rotulo in enumerate(rotulos_raca):
        print(f"Porcentagem de alunos de cor/raça {rotulo}: {row[i]:.1f}%")
    print()

cores = ["#D04CF0", "#6BAFEF", "#8512F0", "#4FF072", "#F0ED4C", "#EF4678"]

ax = dados_porcentagem.plot(kind="bar", stacked=True, figsize=(10, 6), color=cores)

ax.legend(rotulos_raca, title="Cor/Raça")

plt.xlabel("Região")
plt.ylabel("Porcentagem de Alunos")
plt.title("Distribuição de Cor/Raça por Região")

ax.set_xticklabels(dados_porcentagem["NO_REGIAO"], rotation=0)

plt.savefig("analise_manuela/grafico_manuela.png")

plt.show()
