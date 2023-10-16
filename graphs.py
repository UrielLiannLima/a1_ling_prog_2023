import matplotlib.pyplot as plt
import numpy as np
import limpar_df as ldf


# Abre o diretório e limpa ele
df = ldf.open_df("data.csv")
working_df = ldf.remove_outliers(ldf.drop_cols("indexes/custom.txt", ldf.drop_cols("indexes/base.txt", df)))

# Pega quais são todos os estados
estados = working_df["SG_UF"].unique()

# Colunas importantes porém não incluidas no gráfico
nao_equip = ["SG_UF", "NO_REGIAO", "SG_UF", "NO_MUNICIPIO", "NO_ENTIDADE", "TP_DEPENDENCIA"]

# Remove as colunas acima e deixa só as de equipamento
equip = [col for col in df.columns if col not in nao_equip]

marcacao = {
    "IN_INTERNET":"Internet",
    "IN_COMPUTADOR":"Computador",
    "IN_EQUIP_COPIADORA":"Copiadora",
    "IN_EQUIP_IMPRESSORA":"Impressora",
    "IN_EQUIP_IMPRESSORA_MULT":"Impressora Multifuncional",
    "IN_EQUIP_SCANNER":"Scanner",
    "IN_EQUIP_NENHUM":"Nenhum",
    "IN_EQUIP_TV":"Televisores",
    "IN_EQUIP_LOUSA_DIGITAL":"Lousa Digital",
    }

# Passa por cada tipo de equipamento
for column, label in marcacao.items():
    # Faz a figure e o eixo do gráfico
    fig, ax = plt.subplots(figsize=(12, 8))

    colormap = plt.cm.get_cmap('tab10', len(estados))

    espacamento = 0.2
    index = range(len(estados))

    qtde_equip = []

    # Passa por cada estado para separa-los
    for estado in estados:
        state_df = working_df[working_df["SG_UF"] == estado]
        qtde_equip.append(state_df[column].sum())

    ax.bar(
        [x for x in index],
        qtde_equip,
        label=label,
        color=colormap(0),
    )

    ax.set_xlabel("Estados")
    ax.set_ylabel("Nº de Escolas")
    ax.set_title(f"Distribuição de {label} por Estado")
    ax.set_xticks(index)
    ax.set_xticklabels(estados)
    ax.legend()

    plt.tight_layout()

    # Salva o gráfico
    plt.savefig(f'{label}_distribution.png')

    # Mostra o plot
    plt.show()