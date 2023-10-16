import limpar_df as ldf
import pandas as pd

try:
    # Recebe o nome do arquivo de dados do usuário
    data_file = input("Arquivo de dados (.csv): ")
    df = ldf.open_df(data_file)

    # Pede o input do usuário
    print("\nComo você quer separar os seus dados?\n\n1: Estatísticas Escolares\n2: Oferta de Matrículas\n3: Customizado")
    option = input("Digite sua opção: ")

    if option == "1":
        # Devolve apenas os dados escolares
        clean_df = ldf.remove_outliers(ldf.drop_cols("indexes/option1.txt", ldf.drop_cols("indexes/base.txt", df)))
        clean_df.to_csv("estatisticas_escolares.csv", index=False)
    elif option == "2":
        # Devolve apenas os dados das matrículas
        clean_df = ldf.remove_outliers(ldf.drop_cols("indexes/option2.txt", ldf.drop_cols("indexes/base.txt", df)))
        clean_df.to_csv("oferta_matriculas.csv", index=False)
    elif option == "3":
        # Devolve dados customizados
        indexes_file = input("Insira seu arquivo de texto com a extensão (.txt): ")
        clean_df = ldf.remove_outliers(ldf.drop_cols(f"/indexes/{indexes_file}", ldf.drop_cols("indexes/base.txt", df)))
        output_file = input("Escolha o nome do arquivo: ")
        clean_df.to_csv(f"{output_file}.csv", index=False)
    else:
        print("EI, ESSA NÃO É UMA OPÇÃO!!!!")
except FileNotFoundError as erro:
    print(f"Arquivo não encontrado: {erro}")
except pd.errors.EmptyDataError as erro:
    print(f"Erro ao ler o arquivo de dados: {erro}")
except pd.errors.ParserError as erro:
    print(f"Erro de análise do arquivo de dados: {erro}")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {str(erro)}")