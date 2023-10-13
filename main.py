import limpar_csv
import pandas

indexes = input("Nome do arquivo de indexação (.txt): ")
dataframe = input("Nome do dataset (.csv): ")

limpar_csv.drop_cols(indexes, dataframe)