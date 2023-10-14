import pandas as pd
import numpy as np
from scipy import stats

def open_df (data_file:str):
    df = pd.read_csv(data_file, encoding="unicode_escape", engine="python", on_bad_lines="skip", sep=";")
    return df

def drop_cols (text_file:str, df):
    with open(text_file) as indexes:
        for line in indexes:
            line = line.strip('\n')
            if line in df.columns:
                df.drop(columns=line, inplace=True)
    return df

def remove_outliers (df, outlier_code=88888):
    outlier_mask = df.isin([outlier_code]).any(axis=1)
    return df[~outlier_mask]