import matplotlib.pyplot as plt
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
import pandas as pd
import re
from wordcloud import WordCloud

# EXAMPLE WITH THE TRANSCRIPTION OF THE STUDIE E3251_GD04

# Insert CSV file from the CVS files folder:
df = pd.read_csv(
    "C:/Users/diego/Desktop/Mis repositorios/qualitative_social_data_analysis/dataframes_folder/E3251_GD04.csv"
)


# Create a cleaning text function. We delete some special icons and more:
def cleaning_text(text: str) -> str:
    text = re.sub(r"\W", " ", str(text))
    text = re.sub(r"\s+[a-zA-Z]\s+", " ", text)
    text = re.sub(r"\s+", " ", text, flags=re.I)
    text = text.lower()

    return text


# Apply our cleaning text function to our dataframe:
df["text_cleaned"] = df.text.apply(cleaning_text)

# Now we need to delete stopwords.
# I downloaded a spanish stopword's bag, but I added some more stopwords that don't give key information:
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
stop_words_span = list(stop_words_span)


# Create a function to drop the stopwords:
def drop_stopwords(texto: str) -> str:
    words = texto.split()
    words_filter = [word for word in words if word.lower() not in stop_words_span]
    return " ".join(words_filter)


# Apply our stopwords droppes to our dataframe:
df["text_cleaned_nstopwords"] = df["text_cleaned"].apply(drop_stopwords)

# Define the documents / text without stopwords:
all_documents = " ".join(df["text_cleaned_nstopwords"])

# Create a Wordcloud for all the documents / text:
wordcloud = WordCloud(
    width=800, height=400, background_color="white", max_words=50
).generate(all_documents)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Wordcloud of all documents")
plt.show()


# Create a function to get Wordcloud to each informer:
def word_cloud_informer(df: pd.DataFrame) -> Wordcloud:
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
        plt.show()


word_cloud_informer(df)
