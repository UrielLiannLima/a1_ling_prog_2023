import pandas as pd

def open_df (data_file:str):
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

    """
    df = pd.read_csv(data_file, encoding="unicode_escape", engine="python", on_bad_lines="skip", sep=";")
    return df

def drop_cols (text_file:str, df):
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

    """
    with open(text_file) as indexes:
        for line in indexes:
            line = line.strip('\n')
            if line in df.columns:
                df.drop(columns=line, inplace=True)
    return df

def remove_outliers (df):
    """
    Recebe um dataframe, cria uma máscara booleana para marcar todos os valores iguais ao código de outlier, e depois remove as linhas que os possuem.

    Parameters
    ----------
    df : Dataframe Pandas
        Dataframe aberto.

    Returns
    -------
    df[~outlier_mask]
        Retorna o dataframe, porém com as linhas que possuem o código de outlier removidas.
    
    """
    outlier_code = 88888
    outlier_mask = df.isin([outlier_code]).any(axis=1)
    return df[~outlier_mask]