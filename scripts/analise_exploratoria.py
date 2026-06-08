import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# leitura da base
df = pd.read_csv("/PA1/data/raw/brasileirao.csv")

print("Dimensão da base:")
print(df.shape)

print("\nColunas:")
print(df.columns)

print("\nPrimeiras linhas:")
print(df.head())

print("\nValores nulos:")
print(df.isnull().sum())

# nomes das colunas principais da sua base
gols_mandante = "goalsht"
gols_visitante = "goalsvt"
temporada = "season"

# criar coluna de resultado
df["resultado"] = np.where(
    df[gols_mandante] > df[gols_visitante], "Mandante",
    np.where(df[gols_mandante] < df[gols_visitante], "Visitante", "Empate")
)

print("\nFrequência de resultados:")
print(df["resultado"].value_counts())

print("\nEstatísticas dos gols:")
print(df[[gols_mandante, gols_visitante]].describe())

# gráfico de resultados
df["resultado"].value_counts().plot(kind="bar")
plt.title("Resultados das Partidas")
plt.xlabel("Resultado")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)  # deixa reto
plt.tight_layout()
plt.show()

# histograma de gols do mandante
plt.hist(df[gols_mandante].dropna(), bins=10)
plt.title("Gols do Mandante")
plt.xlabel("Gols")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()

# média por temporada
media_temporada = df.groupby(temporada)[[gols_mandante, gols_visitante]].mean()

print("\nMédia de gols por temporada:")
print(media_temporada)

media_temporada.plot()
plt.title("Média de Gols por Temporada")
plt.xlabel("Temporada")
plt.ylabel("Média de gols")
plt.tight_layout()
plt.show()

# comparação geral
print("\nMédia geral de gols do mandante:", df[gols_mandante].mean())
print("Média geral de gols do visitante:", df[gols_visitante].mean())

#Variância
print("\nVariância dos gols do mandante:")
print(df[gols_mandante].var())

print("\nVariância dos gols do visitante:")
print(df[gols_visitante].var())

#Boxplot (Outliers)
plt.boxplot([
    df[gols_mandante].dropna(),
    df[gols_visitante].dropna()
])

plt.title("Boxplot de Gols")
plt.xticks([1, 2], ["Mandante", "Visitante"])
plt.ylabel("Gols")
plt.tight_layout()
plt.show()

#Clubes com mais vitórias
# vitórias do mandante
vitorias_casa = df[df[gols_mandante] > df[gols_visitante]]

ranking_vitorias = vitorias_casa["hometeam"].value_counts().head(10)

print("\nClubes com mais vitórias em casa:")
print(ranking_vitorias)

ranking_vitorias.plot(kind="bar")

plt.title("Clubes com Mais Vitórias")
plt.xlabel("Clubes")
plt.ylabel("Vitórias")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
