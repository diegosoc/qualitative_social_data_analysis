import pandas as pd
import plotly.express as px

#EXAMPLE WITH THE TRANSCRIPTION OF THE STUDIE E3251_GD04

# Insert CSV file from the CVS files folder:
df = pd.read_csv('C:/Users/diego/Desktop/Mis repositorios/qualitative_social_data_analysis/dataframes_folder/E3251_GD04.csv')

# Count times each informer speak:
informers_count = df['informer'].value_counts().reset_index()
informers_count.columns = ['informer', 'count']

# Sort the information min - max:
informers_count = informers_count.sort_values(by='count')

# Create barchart:
fig = px.bar(informers_count, x='informer', y='count')
fig.update_layout(
    title={'text': 'Informer Interventions', 'x': 0.5, 'y': 0.95, 'xanchor': 'center', 'yanchor': 'top'},
    xaxis_title='Informer',
    yaxis_title='nº Interventions',
    font=dict(family='Arial', size=14, color='black')
)
fig.update_traces(textposition='outside', texttemplate='%{y}', cliponaxis=False)
fig.show()
