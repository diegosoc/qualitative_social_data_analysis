import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


stop_words_espanol = set(stopwords.words('spanish'))
stopwords_add = ['tal', 'vez', 'todo', 'toda', 'todos', 'todas', 'tal', 'si', 'no', 'sí', 'creo', 'cómo', 'decía', 'año', 'tema', 'entonces',
                 'claor', 'bueno', 'decir', 'ahora', 'aquí','sé', 'día', 'puede', 'ejemplo', 'claro', 'gente', 'cosa', 'después', 'ver',
                 'eh', 'pues', 'quiero', 'dice', 'cosas', 'momento', 'mucha', 'años', 'mucho', 'muchas', 'muchos', 'bien', 'hecho', 'ser', 'ir',
                 'mejor', 'así', 'gusta', 'alguien', 'hablando', 'ser', 'dices', 'veces', 'siempre', 'persona', 'vale', 'gustaría', 'parece',
                 'menos', 'voy', 'hace', 'hacer', 'depende', 'digamos', 'tampoco', 'va', 'cada', 'mismo', 'digo', 'sido', 'dónde', 'veo',
                 'seguimos', 'da', 'de', 'dé', 'aquel', 'tan', 'mas', 'más']


#Cleaning text function. We delete some special icons and other things.
def cleaning_text(text):

 text = re.sub(r'\W', ' ', str(text))
 text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
 text = re.sub(r'\s+', ' ', text, flags=re.I)
 text = text.lower()

 return text

#Apply our cleaning text function to our dataframe
df_cleaned = df
df_cleaned["text_cleaned"] = df_cleaned.text.apply(cleaning_text)
df_cleaned.head(10)


#Create a function to drop the stopwords:
def drop_stopwords(texto):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words_esp]
    return ' '.join(palabras_filtradas)


#Apply our stopwords droppes to our dataframe:
df_cleaned['text_cleaned_nstopwords'] = df['text_cleaned'].apply(drop_stopwords)
df_cleaned.head(10)


#Create a function to get Wordcloud to each informer:
def word_cloud_informer (df):
  informers = df['informer'].unique()
  for informer in informers:
    df_to_use = df[df['informer'] == informer]
    todos_los_mensajes = ' '.join(df_to_use['text_cleaned_nstopwords'])
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=50).generate(todos_los_mensajes)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Wordcloud of {informer}')
    plt.show()
    
word_cloud_informer(df_cleaned)