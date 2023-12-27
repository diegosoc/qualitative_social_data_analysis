import numpy as np
import pandas as pd
import plotly.graph_objects as go
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
nltk.download('stopwords')

# One of the most important information that we can get from some documents is the key terms.
# Using TF-IDF metrics we can see which terms are most important.
# It can be usefull for social scientist. We can se, for the informers, the most important termins used by each one:

stop_words_espanol = set(stopwords.words('spanish'))

stopwords_add = ['tal', 'vez', 'todo', 'toda', 'todos', 'todas', 'tal', 'si', 'no', 'sí', 'creo', 'cómo', 'decía', 'año', 'tema', 'entonces',
                 'claor', 'bueno', 'decir', 'ahora', 'aquí','sé', 'día', 'puede', 'ejemplo', 'claro', 'gente', 'cosa', 'después', 'ver',
                 'eh', 'pues', 'quiero', 'dice', 'cosas', 'momento', 'mucha', 'años', 'mucho', 'muchas', 'muchos', 'bien', 'hecho', 'ser', 'ir',
                 'mejor', 'así', 'gusta', 'alguien', 'hablando', 'ser', 'dices', 'veces', 'siempre', 'persona', 'vale', 'gustaría', 'parece',
                 'menos', 'voy', 'hace', 'hacer', 'depende', 'digamos', 'tampoco', 'va', 'cada', 'mismo', 'digo', 'sido', 'dónde', 'veo',
                 'seguimos', 'da', 'de', 'dé', 'aquel', 'tan', 'mas', 'más']

stop_words_espanol.update(stopwords_add)

# Transform set into list:
stop_words_esp = list(stop_words_espanol)

def tfidf_informer(df: pd.DataFrame) -> bar charts:
    # Extract the informers index:
    informers = df['informer'].unique()

    # Calculate the TF-IDF for each informer:
    for informer in informers:
        df_to_use = df[df['informer'] == informer]
        tfidf_vectorizer = TfidfVectorizer(stop_words = stop_words_esp)
        tfidf_matrix = tfidf_vectorizer.fit_transform(df_to_use['text_cleaned'])
        feature_names = tfidf_vectorizer.get_feature_names_out()
        av_tfidf_metrics = np.mean(tfidf_matrix, axis=0).tolist()[0]
        metrics = list(zip(feature_names, av_tfidf_metrics))

        # TF-IDF average sorted:
        sorted_metrics = sorted(puntuaciones, key=lambda x: x[1], reverse=True)
        metrics_dict = dict(sorted(puntuaciones_ordenadas[:7], key=lambda x: x[1], reverse=True))
        terms = [f"{metrics_dict[term]:.3f}" for term in metrics_dict]

        # Create charts for each informer:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=list(metrics_dict.values()),
            y=list(metrics_dict.keys()),
            orientation='h',
            text = terms,
            textposition = 'outside',
            marker = dict(color='purple')
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
            xaxis_range=[0, max(puntuaciones_dict.values()) + 0.05],
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
