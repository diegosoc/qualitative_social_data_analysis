import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_informer(df):
    informers = df['informer'].unique()
    for informer in informers:
        df_to_use = df[df['informer'] == informer]

        tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words_esp)

        tfidf_matrix = tfidf_vectorizer.fit_transform(df_to_use['text_cleaned'])

        feature_names = tfidf_vectorizer.get_feature_names_out()

        puntuaciones_medias = np.mean(tfidf_matrix, axis=0).tolist()[0]
        puntuaciones = list(zip(feature_names, puntuaciones_medias))

        # TF-IDF average sorted:
        puntuaciones_ordenadas = sorted(puntuaciones, key=lambda x: x[1], reverse=True)

        puntuaciones_dict = dict(sorted(puntuaciones_ordenadas[:7], key=lambda x: x[1], reverse=True))

        etiquetas = [f"{puntuaciones_dict[termino]:.3f}" for termino in puntuaciones_dict]

        # Create charts for each informer:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=list(puntuaciones_dict.values()),
            y=list(puntuaciones_dict.keys()),
            orientation='h',
            text=etiquetas,
            textposition='outside',
            marker=dict(color='purple')
        ))

        fig.update_layout(
            title={
                'text': f'Most important terms for {informer}',
                'font': {'size': 18, 'family': 'Arial', 'color': 'black'},
                'x': 0.5,
                'y': 0.9
            },
            xaxis_title='TF-IDF score average',
            yaxis_title='Terms',
            xaxis_range=[0, max(puntuaciones_dict.values()) + 0.05],  # Ajusta según tus datos
            yaxis={
                'autorange': 'reversed',
                'tickfont': {'size': 16},
            },
            font={
                'size': 14,
            }
        )

        fig.show()

tfidf_informer(df_cleaned)