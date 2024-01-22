import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import pandas as pd
import re
from wordcloud import WordCloud
nltk.download("stopwords")

# EXAMPLE WITH THE TRANSCRIPTION OF THE STUDIE E3251_GD04

# Create a cleaning text function which we delete some special icons and more:
def cleaning_text(text: str) -> str:
    text = re.sub(r"\W", " ", str(text))
    text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)
    text = re.sub(r"\s+", " ", text, flags=re.I)
    text = text.lower()

    return text

# Create the stopwords list:
def create_stopwords_span ():
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
    stop_words_span = list(stop_words_span)

    return stop_words_span

# Create a function to drop the stopwords:
def drop_stopwords(text: str):
    stop_words_span = create_stopwords_span ()
    words = text.split()
    words_filter = [word for word in words if word.lower() not in stop_words_span]

    return " ".join(words_filter)

# Create a Wordcloud for all the documents / text:
def word_cloud_global (df: pd.DataFrame):

    df["text_cleaned"] = df.text.apply(cleaning_text)
    df["text_cleaned_nstopwords"] = df["text_cleaned"].apply(drop_stopwords)
    all_documents = " ".join(df["text_cleaned_nstopwords"])

    wordcloud = WordCloud(
        width=800, height=400, background_color="white", max_words=50
    ).generate(all_documents)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Wordcloud of all documents")

    return plt.show()


# Create a function to get Wordcloud to each informer:
def word_cloud_informer(df: pd.DataFrame):

    df["text_cleaned"] = df.text.apply(cleaning_text)
    df["text_cleaned_nstopwords"] = df["text_cleaned"].apply(drop_stopwords)
    informers = df["informer"].unique()

    for informer in informers:
        df_to_use = df[df["informer"] == informer]
        todos_los_mensajes = " ".join(df_to_use["text_cleaned_nstopwords"])
        wordcloud = WordCloud(
            width=800, height=400, background_color="white", max_words=50
        ).generate(todos_los_mensajes)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title(f"Wordcloud of {informer}")

    return plt.show()

if __name__ == '__main__':
    df = pd.read_csv('')
    word_cloud_global(df)
    word_cloud_informer(df)
