import matplotlib.pyplot as plt
import numpy as np
import limpar_df as ldf

# Abrir o arquivo de dados e estruturação
df = ldf.open_df("data.csv")
structure_df = ldf.remove_outliers(ldf.drop_cols("indexes/custom.txt", ldf.drop_cols("indexes/base.txt", df)))

# Busca as regiões do país
regioes = structure_df["NO_REGIAO"].unique()

marcacao = {
    "IN_AGUA_INEXISTENTE": "Água",
    "IN_ENERGIA_INEXISTENTE": "Energia",
    "IN_ESGOTO_INEXISTENTE": "Esgotamento Sanitário",
    "IN_LIXO_SERVICO_COLETA": "Coleta de Lixo",
    "IN_BANHEIRO": "Banheiro",
    "IN_BIBLIOTECA": "Biblioteca",
    "IN_LABORATORIO_INFORMATICA": "Laboratório de Informática",
    "IN_QUADRA_ESPORTES": "Quadra de Esportes",
    "IN_SALA_DIRETORIA": "Sala de Diretoria",
    "IN_SALA_PROFESSOR": "Sala de Professores",
    "IN_SECRETARIA": "Secretaria",
    "IN_ACESSIBILIDADE_INEXISTENTE": "Recursos de Acessibilidade",
    "IN_ALIMENTACAO": "Alimentação",
    "IN_MATERIAL_PED_NENHUM": "Materiais Pedagógicos"
}

# Calcula o número total de escolas por região
total_escolas_por_regiao = [len(structure_df[structure_df["NO_REGIAO"] == regiao]) for regiao in regioes]

# Itera todas as regiões
for i, regiao in enumerate(regioes):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    labels = []
    qtde_infra = []

    # Adiciona a label com o número total de escolas por região
    labels.append(f"Total de Escolas: {total_escolas_por_regiao[i]}")
    qtde_infra.append(total_escolas_por_regiao[i])

    for column, label in marcacao.items():
        reg_df = structure_df[structure_df["NO_REGIAO"] == regiao]
        total_escolas = len(reg_df)  # Total de escolas na região
        value = reg_df[column].sum()
        
        #Corrige os dados que vinham invertidos, com o final "_INEXISTENTE"
        if label in ["Água", "Energia", "Esgotamento Sanitário", "Recursos de Acessibilidade", "Materiais Pedagógicos"]:
            value = total_escolas - value

        # Adiciona o número total para cada label
        labels.append(f"{label}: {value}")
        qtde_infra.append(value)

    index = np.arange(len(labels))

    ax.bar(
        index,
        qtde_infra,
    )

    ax.set_xlabel("Infraestrutura")
    ax.set_ylabel("Nº de Escolas")
    ax.set_title(f"Distribuição de Infraestrutura por Região: {regiao}")

    ax.set_xticks(index)
    ax.set_xticklabels(labels, rotation=45, ha='right')

    plt.tight_layout()

    # Salva o gráfico para cada região
    plt.savefig(f'{regiao}_distribution.png')

    # Mostra o plot
    plt.show()


