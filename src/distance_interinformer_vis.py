from bertopic import BERTopic
import matplotlib.pyplot as plt
import nltk
import numpy as np
from nltk.corpus import stopwords
import pandas as pd
import plotly.express as px
import re
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer

nltk.download("stopwords")

# EXAMPLE WITH THE TRANSCRIPTION OF THE STUDIE E3251_GD04

def limpiar_texto(text: str):
    text = re.sub(r"\W", " ", str(text))
    text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)
    text = re.sub(r"\s+", " ", text, flags=re.I)
    text = text.lower()

    return texto

def remove_stopwords(text: str):
    stop_words_span = set(stopwords.words("spanish"))
    stopwords_add = [
        "dos", "tal", "vez", "todo", "toda", "todos", "todas", "tal", "si", "no", "sí", "creo", "cómo", "decía",
        "año", "tema", "entonces", "claor", "bueno", "decir", "ahora", "aquí", "sé", "día", "puede", "ejemplo",
        "claro", "gente", "cosa", "después", "ver", "eh", "pues", "quiero", "dice", "cosas", "momento", "mucha",
        "años", "mucho", "muchas", "muchos", "bien", "hecho", "ser", "ir", "mejor", "así", "gusta", "alguien",
        "hablando", "ser", "dices", "veces", "siempre", "persona", "vale", "gustaría", "parece", "menos", "voy",
        "hace", "hacer", "depende", "digamos", "tampoco", "va", "cada", "mismo", "digo", "sido", "dónde", "veo",
        "seguimos", "da", "de", "dé", "aquel", "tan", "mas", "más",
    ]
    stop_words_span.update(stopwords_add)
    stop_words_span = set(stop_words_span)

    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words_span]

    return ' '.join(filtered_words)

def get_df_with_embeddings_reduced (df):
    model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
    embeddings_list = []
    for x in df['text']:
        embeddings_df.append(model.encode(x))

    '''
    Now we can reduce the embeddings dimensionality by using T-SNE algorithm.
    You can change the random seed.
    
    '''
    your_seed_value = 100
    np.random.seed(your_seed_value)
    tsne = TSNE(n_components=2)
    embeddings_reduced = tsne.fit_transform(np.array(embeddings_list))
    return embeddings_reduced
    
def main (): 
    df = pd.read_csv('E3251_GD04.csv')
    df['text'] = df['text'].apply(limpiar_texto)
    df['text'] = df['text'].apply(remove_stopwords)
    df[['PC1', 'PC2']] = pd.DataFrame(get_df_with_embeddings_reduced(), columns=['PC1', 'PC2'])
    centroides = df.groupby('informer').agg({'PC1': 'mean', 'PC2': 'mean'}).reset_index()
    fig = px.scatter(centroides, x='PC1', y='PC2', color='informer', size=[10]*len(centroides), title='Inter-informer distance')
    fig.update_layout(xaxis_title='PC1', yaxis_title='PC2')
    axis = 11
    fig.update_yaxes(range=[-axis, axis])
    fig.update_xaxes(range=[-axis, axis])

    # Mostrar el gráfico
    fig.show()

if __name__ == "__main__":
    main()