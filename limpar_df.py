import pandas as pd

def open_df (data_file: str):
    """
    Abre o arquivo de dados como um dataframe Pandas.

    Parameters
    ----------
    data_file : string
        Nome do arquivo de dados

    Returns
    -------
    df : Dataframe Pandas
        Retorna o dataframe aberto
    
    >>> # Teste normal
    >>> with open("teste.csv", "w") as file: file.write("A;B;C\\n1;2;3\\n4;5;6")
    >>> df = open_df("teste.csv")
    >>> df.shape
    (2, 3)
    >>> import os
    >>> os.remove("teste.csv")
    """
    try:
        df = pd.read_csv(data_file, encoding="unicode_escape", engine="python", on_bad_lines="skip", sep=";")
        return df
    except FileNotFoundError as erro:
        print(f"Arquivo não encontrado: {erro}")
        return None
    except pd.errors.EmptyDataError as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        return None
    except pd.errors.ParserError as erro:
        print(f"Erro ao analisar os dados: {erro}")
        return None
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        return None

def drop_cols (text_file: str, df):
    """
    Remove as colunas do dataframe recebido com os indexes recebidos do arquivo de texto.

    Parameters
    ----------
    text_file : string
        Nome do arquivo de texto com os indexes
    df : Dataframe Pandas
        Dataframe aberto

    Returns
    -------
    df : Dataframe Pandas
        Dataframe com as colunas especificadas no arquivo de texto dropadas
    
    >>> # Teste normal da função
    >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    >>> with open("index.txt", "w") as file:
    ...     file.write("A\\nC")
    >>> new_df = drop_cols("index.txt", df)
    >>> new_df.columns.to_list()
    ['B']
    >>> import os
    >>> os.remove("index.txt")
    
    >>> # Teste com um index vazio
    >>> empty_index = ""
    >>> with open("empty_index.txt", "w") as file:
    ...     file.write(empty_index)
    >>> new_df = drop_cols("empty_index.txt", df)
    >>> new_df.columns.to_list()
    ['A', 'B', 'C']
    >>> import os
    >>> os.remove("empty_index.txt")
    
    >>> # Teste de index com colunas que não existem
    >>> with open("invalid_index.txt", "w") as file:
    ...     file.write("X\\nY")
    >>> new_df = drop_cols("invalid_index.txt", df)
    >>> new_df.columns.to_list()
    ['A', 'B', 'C']
    >>> import os
    >>> os.remove("invalid_index.txt")
    """
    try:
        with open(text_file) as indexes:
            for line in indexes:
                line = line.strip('\n')
                if line in df.columns:
                    df.drop(columns=line, inplace=True)
        return df
    except FileNotFoundError as erro:
        print(f"Arquivo de index não encontrado: {erro}")
        return None
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        return None

def remove_outliers (df):
    """
    Recebe um dataframe, cria uma máscara booleana para marcar todos os valores iguais ao código de outlier e depois remove as linhas que os possuem.

    Parameters
    ----------
    df : Dataframe Pandas
        Dataframe aberto.

    Returns
    -------
    df[~outlier_mask]
        Retorna o dataframe, porém com as linhas que possuem o código de outlier removidas.
    
    >>> # Teste normal
    >>> df = pd.DataFrame({"A": [1, 2, 3, 88888], "B": [4, 5, 6, 7]})
    >>> cleaned_df = remove_outliers(df)
    >>> cleaned_df.shape
    (3, 2)
    
    >>> # Teste sem outliers
    >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    >>> cleaned_df = remove_outliers(df)
    >>> cleaned_df.shape
    (3, 2)
    """
    try:
        outlier_code = 88888
        outlier_mask = df.isin([outlier_code]).any(axis=1)
        return df[~outlier_mask]
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        return None

# Unit test para o módulo
def testar_open_df ():
    # Cria um csv para o teste utilizando dados de amostra
    amostra = "A;B;C\n1;2;3\n4;5;6"
    with open("teste.csv", "w") as file:
        file.write(amostra)

    df = open_df("teste.csv")
    assert df.shape == (2, 3)

    # Remove o arquivo usado no teste
    import os
    os.remove("teste.csv")

def testar_drop_cols ():
    # Cria um dataframe de teste e um arquivo de texto para os indexes
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    with open("index.txt", "w") as file:
        file.write("A\nC")

    new_df = drop_cols("index.txt", df)
    assert new_df.columns.to_list() == ["B"]

    # Remove o arquivo usado no teste
    import os
    os.remove("index.txt")

def testar_remove_outliers ():
    # Cria um dataframe de exemplo com o código de outlier
    df = pd.DataFrame({"A": [1, 2, 3, 88888], "B": [4, 5, 6, 7]})

    cleaned_df = remove_outliers(df)
    assert cleaned_df.shape == (3, 2)

if __name__ == "__main__":
    testar_open_df()
    testar_drop_cols()
    testar_remove_outliers()
    import doctest
    doctest.testmod()
    print("Teste Completo.")
