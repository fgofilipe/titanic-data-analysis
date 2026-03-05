#Projeto: Análise Exploratória de Dados - Titanic
#Curso: Introdução ao Data Science
#Aluno: Filipe de Oliveira Gomes

import pandas as pd
import matplotlib.pyplot as plt
import os


caminho_base = os.path.dirname(__file__)
caminho_csv = os.path.join(caminho_base, "titanic_dataset.csv")

df = pd.read_csv(caminho_csv)

print("\nDimensões do dataset:")
print(df.shape)

print("\nPrimeiras linhas do dataset:")
print(df.head())


print("\nInformações gerais:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

print("\nValores nulos por coluna:")
print(df.isnull().sum())


df["Age"].fillna(df["Age"].mean(), inplace=True)

df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

df.drop(columns=["Cabin"], inplace=True)

df.drop_duplicates(inplace=True)


survival_rate = df["Survived"].mean()
print(f"\nTaxa geral de sobrevivência: {survival_rate:.2f}")

# VISUALIZAÇÃO

survival_by_sex = df.groupby("Sex")["Survived"].mean()
print("\nSobrevivência por sexo:")
print(survival_by_sex)

survival_by_class = df.groupby("Pclass")["Survived"].mean()
print("\nSobrevivência por classe:")
print(survival_by_class)

print("\nIdade média por sobrevivência:")
print(df.groupby("Survived")["Age"].mean())


def grafico_sobrevivencia_sexo(df):

    survival_by_sex = df.groupby("Sex")["Survived"].mean()

    plt.figure()
    survival_by_sex.plot(kind="bar")

    plt.title("Taxa de Sobrevivência por Sexo")
    plt.xlabel("Sexo")
    plt.ylabel("Taxa de Sobrevivência")

    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.show()

def grafico_distribuicao_idade(df):

    plt.figure()

    df["Age"].hist(bins=20)

    plt.title("Distribuição de Idades dos Passageiros")
    plt.xlabel("Idade")
    plt.ylabel("Quantidade")

    plt.tight_layout()

    plt.show()  

grafico_sobrevivencia_sexo(df)
grafico_distribuicao_idade(df)

print("\nAnálise concluída com sucesso.")