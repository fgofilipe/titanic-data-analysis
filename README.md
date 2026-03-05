# Análise Exploratória de Dados - Titanic

## Objetivo

O objetivo deste projeto foi realizar uma Análise Exploratória de Dados (AED) utilizando a base pública do Titanic. A proposta consiste em importar, organizar e analisar os dados com o objetivo de compreender o comportamento das informações e identificar possíveis fatores relacionados à sobrevivência dos passageiros.

## Importação e exploração dos dados

A análise foi realizada utilizando a linguagem Python e as bibliotecas Pandas e Matplotlib. Inicialmente, o conjunto de dados foi importado a partir de um arquivo CSV. Após a importação, foram realizadas etapas de exploração inicial dos dados, incluindo a verificação das dimensões do dataset, visualização das primeiras linhas, análise das informações gerais das colunas e estatísticas descritivas.

Essas etapas permitiram compreender melhor a estrutura da base de dados, identificar os tipos de variáveis presentes e observar possíveis inconsistências ou valores ausentes.

## Tratamento de dados

Durante a análise inicial foram identificados valores nulos em algumas colunas da base de dados. Para tratar esses problemas foram adotadas algumas estratégias:

- Substituição dos valores nulos da coluna **Age** pela média das idades.
- Substituição dos valores nulos da coluna **Embarked** pelo valor mais frequente.
- Remoção da coluna **Cabin**, pois ela apresentava grande quantidade de dados ausentes.
- Verificação e remoção de possíveis registros duplicados.

Essas etapas foram importantes para garantir maior consistência e qualidade dos dados antes da realização das análises.

## Análise exploratória

Após o tratamento dos dados, foram realizadas algumas análises exploratórias com o objetivo de identificar padrões e relações entre as variáveis presentes no dataset.

Entre as análises realizadas estão:

- Cálculo da taxa geral de sobrevivência dos passageiros.
- Análise da taxa de sobrevivência por sexo.
- Análise da sobrevivência de acordo com a classe do passageiro.
- Cálculo da idade média entre passageiros que sobreviveram e os que não sobreviveram.

Essas análises foram realizadas utilizando operações de agrupamento (GroupBy) e estatísticas básicas da biblioteca Pandas.

## Visualização de dados

Além das análises numéricas, também foram geradas visualizações gráficas para facilitar a interpretação dos dados.

Foram criados dois gráficos principais:

- Gráfico de barras mostrando a taxa de sobrevivência por sexo.
- Histograma apresentando a distribuição das idades dos passageiros.

As visualizações foram geradas utilizando a biblioteca Matplotlib.

## Conclusão

A análise exploratória permitiu identificar alguns padrões relevantes na base de dados do Titanic. Observou-se que fatores como sexo e classe social parecem ter influenciado as chances de sobrevivência dos passageiros.

A utilização de ferramentas de análise de dados em Python possibilitou explorar o dataset de forma estruturada, identificar padrões e gerar visualizações que facilitam a interpretação das informações presentes na base.