import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Permite puxar do módulo 1 diretório acima para importar o limpar_df
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import limpar_df as ldf

# Abre o diretório e remove as colunas não utilizadas como também as linhas com outliers
df = ldf.open_df("../data.csv")
working_df = ldf.remove_outliers(ldf.drop_cols("not_used.txt", df))
    
#contando o número de matriculas por raça, foi dividido por um milhão para facilitar a visualização
parabolica = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_ND"].sum)
computador = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_BRANCA"].sum)
copiadora = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_PRETA"].sum)
impressora = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_PARDA"].sum)
impressora_mult = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_AMARELA"].sum)
scanner = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
nenhum = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
dvd = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
som = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
tv = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
lousa_digital = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
multimidia = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
desktop_aluno = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
comp_portatil_aluno = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)
tablet_aluno = (df.groupby("TP_DEPENDENCIA")["QT_MAT_BAS_INDIGENA"].sum)

#Gera a figura
figura = plt.figure()
#ajusta o tamanho das barras
barWidht=0.13
#Ajusta a posição das barras de cada variável
p1 = np.arange(len(nao_declarada))
p2 = [x + barWidht for x in p1]
p3 = [x + barWidht for x in p2]
p4 = [x + barWidht for x in p3]
p5 = [x + barWidht for x in p4]
p6 = [x + barWidht for x in p5]
#plota o gráfico das 6 variáveis
plt.bar(p1, nao_declarada, label="Não Declarada", color="#A569BD", width=barWidht)
plt.bar(p2, branca, label="Branca", color="#F4D03F", width=barWidht)
plt.bar(p3, preta, label="Preta", color="#3498DB", width=barWidht)
plt.bar(p4, parda, label="Parda", color="#E74C3C", width=barWidht)
plt.bar(p5, amarela, label="Amarela", color="#58D68D", width=barWidht)
plt.bar(p6, indigena, label="Indígena", color="#7F8C8D", width=barWidht)
plt.ylim(0, 10)
plt.title("Número de matrículas na educação básica, por tipo de escola")
plt.xlabel("Tipo de escola")
#Nomeia o eixo x com o tipo de escola
plt.xticks([p + barWidht for p in range(len(var1))], ["Federal", "Municipal","Estadual", "Privada"])
plt.ylabel("Número de matriculas (em milhões)")
#adiciona legenda ao gráfico, pois são várias variáveis
plt.legend()
#mostra a figura
plt.show()
#salva a figura
figura.savefig("analise_alessandra/grafico_Ale.png")

#print dos dados, para análise
print ("Matrículas de pessoas da raça Não declarada: ", nao_declarada, "Matrículas de pessoas da raça Branca: ", branca,
       "Matrículas de pessoas da raça Preta: ", preta, "Matrículas de pessoas da raça Parda: ", parda, 
       "Matrículas de pessoas da raça Amarela: ", amarela, "Matrículas de pessoas da raça Indígena: ", indigena, sep="\n\n")