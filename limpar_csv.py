import pandas as pd

def drop_cols (text_file:str, csv_file:str):
    """
    Parameters
    ----------
    text_file : str
        Arquivo de texto com a indexação das colunas a serem removidas
    csv_file : str
        Dataframe em formato csv que vai ter as colunas dropadas

    Returns
    -------
    print("Done")
        Retorna no terminal "Done" para demonstrar que o processo foi feito com sucesso
    """
    df = pd.read_csv(csv_file, encoding="unicode_escape", engine="python", on_bad_lines="skip", sep=";")
    print(df.head())
    print(df.tail())
    with open(text_file) as indexes:
        for line in indexes:
            line = line.strip('\n')
            if line in df.columns:
                df.drop(columns=line, inplace=True)
    print(df.head())
    print(df.tail())
    df.to_csv("clean_data.csv", index=False)
    return print("Done")

