import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
drinks_csv = pd.read_csv('../Web Scrapers/drinks.csv')

# Calculando a média de litros de álcool puro
media = drinks_csv['total_litres_of_pure_alcohol'].mean()

# Filtrando os países que consomem acima da média
data_frame = drinks_csv.query(f'total_litres_of_pure_alcohol >= {media}').sort_values('total_litres_of_pure_alcohol',
                                                                                      ascending=False)[['country', 'total_litres_of_pure_alcohol']]

# Configurando o tamanho do gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Construindo o gráfico de barras
ax.bar(data_frame['country'], data_frame['total_litres_of_pure_alcohol'])

# Configurando o título do gráfico e dos eixos
ax.set_xticklabels(data_frame['country'], fontsize=5, rotation=90)
ax.set_title('Consumo de Álcool em Países Selecionados')
ax.set_xlabel('País', fontsize=12)
ax.set_ylabel('Total de Litros de Álcool Puro', fontsize=12)

# Rotacionando as legendas do eixo x em 90 graus
plt.xticks(rotation=90)

# Exibindo o gráfico
plt.tight_layout()
plt.show()
