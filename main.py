import limpar_df as ldf
import pandas as pd

indexes = input("Nome do arquivo de indexação (.txt): ")
df = ldf.open_df(input("Arquivo de dados (.csv): "))

clean_df = ldf.remove_outliers(ldf.drop_cols(indexes, df))
clean_df.to_csv("clean_data.csv", index=False)

print(clean_df.head())
print(clean_df.tail())