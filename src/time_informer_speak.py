#IDEAS:
#Times each participant speak
#How long do the participants speak
#Which are the most relevant topics in each kkey question
#Which are the most relevant topics in each participant in all the GD
#Which sentiment is the most relevant in all the GD / each key question / each participant

import pandas as pd
import plotly.express as px

#Insetar archivo o archivos concretos a tratar de la carpeta con CSVs files
df = pd.read_csv('C:/Users/diego/Desktop/Mis repositorios/qualitative_social_data_analysis/gd1/E3251_GD01.csv')

# Contar la cantidad de mensajes por informer
informers_count = df['informer'].value_counts().reset_index()
informers_count.columns = ['informer', 'count']

# Ordenar los informers de menor a mayor
informers_count = informers_count.sort_values(by='count')

# Crear un gráfico de barras con Plotly Express
fig = px.bar(informers_count, x='informer', y='count')

# Personalizar el título y los ejes
fig.update_layout(
    title={'text': 'Cantidad de Mensajes por Informer', 'x': 0.5, 'y': 0.95, 'xanchor': 'center', 'yanchor': 'top'},
    xaxis_title='Informer',
    yaxis_title='Cantidad de Mensajes',
    font=dict(family='Arial', size=14, color='black')  # Establecer el texto en negrita
)

# Personalizar las etiquetas de valor por encima de las barras
fig.update_traces(textposition='outside', texttemplate='%{y}', cliponaxis=False)

# Mostrar el gráfico
fig.show()