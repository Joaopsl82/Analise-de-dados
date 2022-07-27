# Importar Base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv('telecom_users.csv')

# Visualizar a base de dados
# Entender as informações que você tem disponível
# Descobrir os erros da base de dados
tabela = tabela.drop('Unnamed: 0', axis=1)

# Tratamento de dados (resolver os erros), informações vazias
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# Valores vazios colunas
tabela = tabela.dropna(how='all', axis=1)
# Valores vazios linhas
tabela = tabela.dropna(how='any', axis=0)

# Análise Inicial dos dados
# Como estão os nossos cancelamentos?
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map("{:.1%}".format))

# Descobrir os motivos do cancelamento
# Comparar cada coluna da minha tabela com a coluna de cancelamento

for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    # etapa 1: Criar gráfico
    grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True, color_discrete_sequence=['red', 'purple'])
    
    # etapa 2: exibir gráfico
    grafico.show()