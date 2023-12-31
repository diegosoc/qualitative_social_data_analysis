import numpy as np
import pandas as pd
import plotly.graph_objects as go
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

nltk.download("stopwords")

# EXAMPLE WITH THE TRANSCRIPTION OF THE STUDIE E3251_GD04

# Insert CSV file from the CVS files folder:
df = pd.read_csv(
    "C:/Users/diego/Desktop/Mis repositorios/qualitative_social_data_analysis/dataframes_folder/E3251_GD04.csv"
)

# One of the most important information that we can get from some documents is the key terms.
# Using TF-IDF metrics we can see which terms are most important.
# It can be usefull for social scientist. We can see, for all the documents and for each informers, the most important termins used by each one:


def cleaning_text(text):
    text = re.sub(r"\W", " ", str(text))
    text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)
    text = re.sub(r"\s+", " ", text, flags=re.I)
    text = text.lower()

    return text


df["text_cleaned"] = df.text.apply(cleaning_text)

stop_words_span = set(stopwords.words("spanish"))

stopwords_add = [
    "dos",
    "tal",
    "vez",
    "todo",
    "toda",
    "todos",
    "todas",
    "tal",
    "si",
    "no",
    "sí",
    "creo",
    "cómo",
    "decía",
    "año",
    "tema",
    "entonces",
    "claor",
    "bueno",
    "decir",
    "ahora",
    "aquí",
    "sé",
    "día",
    "puede",
    "ejemplo",
    "claro",
    "gente",
    "cosa",
    "después",
    "ver",
    "eh",
    "pues",
    "quiero",
    "dice",
    "cosas",
    "momento",
    "mucha",
    "años",
    "mucho",
    "muchas",
    "muchos",
    "bien",
    "hecho",
    "ser",
    "ir",
    "mejor",
    "así",
    "gusta",
    "alguien",
    "hablando",
    "ser",
    "dices",
    "veces",
    "siempre",
    "persona",
    "vale",
    "gustaría",
    "parece",
    "menos",
    "voy",
    "hace",
    "hacer",
    "depende",
    "digamos",
    "tampoco",
    "va",
    "cada",
    "mismo",
    "digo",
    "sido",
    "dónde",
    "veo",
    "seguimos",
    "da",
    "de",
    "dé",
    "aquel",
    "tan",
    "mas",
    "más",
]

stop_words_span.update(stopwords_add)

# Transform set into list:
stop_words_esp = list(stop_words_span)

# Create the TD-IDF model and fit for ALL documents:
tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words_span)
tfidf_matrix = tfidf_vectorizer.fit_transform(df["text_cleaned"])
feature_names = tfidf_vectorizer.get_feature_names_out()
av_metrics = np.mean(tfidf_matrix, axis=0).tolist()[0]
metrics = list(zip(feature_names, av_metrics))
sorted_metrics = sorted(metrics, key=lambda x: x[1], reverse=True)

# Show first 10 most important terms in all the documents:
for term, metric in sorted_metrics[:10]:
    print(f"{term}: {metric}")

# Visualization TF-IDF information:
# Create a dictionary with the sorted terms and their TF-IDF metrics of all documents:
metrics_dict = dict(sorted(sorted_metrics[:7], key=lambda x: x[1], reverse=True))
terms = [f"{metrics_dict[term]:.3f}" for term in metrics_dict]

# Create barchart for TF-IDF metrics for all documents
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=list(metrics_dict.values()),
        y=list(metrics_dict.keys()),
        orientation="h",
        text=terms,
        textposition="outside",
        marker=dict(color="purple"),
    )
)
fig.update_layout(
    title={
        "text": "Most important terms in all documents",
        "font": {"size": 18, "family": "Arial", "color": "black"},
        "x": 0.5,
        "y": 0.9,
    },
    xaxis_title="TF-IDF score average",
    yaxis_title="Terms",
    xaxis_range=[0, max(metrics_dict.values()) + 0.02],
    yaxis={
        "autorange": "reversed",
        "tickfont": {"size": 16},
    },
    font={
        "size": 14,
    },
)
fig.show()

# Create a function to get TF-IDF information of each informer:


def tfidf_informer(df: pd.DataFrame):
    # Extract the informers index:
    informers = df["informer"].unique()

    # Calculate the TF-IDF for each informer:
    for informer in informers:
        df_to_use = df[df["informer"] == informer]
        tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words_esp)
        tfidf_matrix = tfidf_vectorizer.fit_transform(df_to_use["text_cleaned"])
        feature_names = tfidf_vectorizer.get_feature_names_out()
        av_tfidf_metrics = np.mean(tfidf_matrix, axis=0).tolist()[0]
        metrics = list(zip(feature_names, av_tfidf_metrics))

        # TF-IDF average sorted:
        sorted_metrics = sorted(metrics, key=lambda x: x[1], reverse=True)
        metrics_dict = dict(
            sorted(sorted_metrics[:7], key=lambda x: x[1], reverse=True)
        )
        terms = [f"{metrics_dict[term]:.3f}" for term in metrics_dict]

        # Create charts for each informer:
        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=list(metrics_dict.values()),
                y=list(metrics_dict.keys()),
                orientation="h",
                text=terms,
                textposition="outside",
                marker=dict(color="purple"),
            )
        )

        fig.update_layout(
            title={
                "text": f"Most important terms for {informer}",
                "font": {"size": 18, "family": "Arial", "color": "black"},
                "x": 0.5,
                "y": 0.9,
            },
            xaxis_title="TF-IDF score average",
            yaxis_title="Terms",
            xaxis_range=[0, max(metrics_dict.values()) + 0.02],
            yaxis={
                "autorange": "reversed",
                "tickfont": {"size": 16},
            },
            font={
                "size": 14,
            },
        )

        fig.show()


tfidf_informer(df)
