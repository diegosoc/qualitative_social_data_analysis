from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
from nltk.corpus import stopwords

# EXAMPLE WITH THE TRANSCRIPTION OF THE STUDIE E3251_GD04

# Insert CSV file from the CVS files folder:


def limpiar_texto(texto):
    texto = re.sub(r"\W", " ", str(texto))
    texto = re.sub(r"\s+[a-zA-Z]\s+", " ", texto)
    texto = re.sub(r"\s+", " ", texto, flags=re.I)
    texto = texto.lower()

    return texto


def create_stopwords_span():
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

    return stop_words_span.update(stopwords_add)


def main():
    df = pd.read_csv(
        "C:/Users/diego/Desktop/Mis repositorios/qualitative_social_data_analysis/dataframes_folder/E3251_GD04.csv"
    )

    df["text_cleaned"] = df.text.apply(limpiar_texto)

    # We can use CountVectorizer or other tool to get the embeddings. In this case I used CountVectorizer:
    stop_words_esp = create_stopwords_span()
    vectorizer_model = CountVectorizer(stop_words=stop_words_esp)
    bert_model = BERTopic(language="spanish", vectorizer_model=vectorizer_model)

    # Fit the model to our data:
    topics, ini_probs = bert_model.fit_transform(df["text_cleaned"])

    # Visualization of bertopic results:
    # 1. Barchart with topics and probabilities:
    bert_model.visualize_barchart(top_n_topics=16, n_words=10)

    # 2. Intertopic distance map:
    bert_model.visualize_topics()

    # 3. Visualization of the topic-clusters:
    bert_model.visualize_documents(df["text_cleaned"])

    # 4. Hierarchical clustering of topics:
    bert_model.visualize_hierarchy()

    # 5. Similarity information (matrix) of the topics:
    bert_model.visualize_heatmap()


if __name__ == "__main__":
    main()
