from bertopic import BERTopic
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import pandas as pd
import plotly.express as px
import re
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')

#EXAMPLE WITH THE TRANSCRIPTION OF THE STUDIE E3251_GD04

# Insert CSV file from the CVS files folder:
df = pd.read_csv('C:/Users/diego/Desktop/Mis repositorios/qualitative_social_data_analysis/dataframes_folder/E3251_GD04.csv')

def limpiar_texto(texto):

 texto = re.sub(r'\W', ' ', str(texto))
 texto = re.sub(r'\s+[a-zA-Z]\s+', ' ', texto)
 texto = re.sub(r'\s+', ' ', texto, flags=re.I)
 texto = texto.lower()

 return texto

df["text_cleaned"] = df.text.apply(limpiar_texto)

stop_words_span = set(stopwords.words('spanish'))
stopwords_add = ['dos', 'tal', 'vez', 'todo', 'toda', 'todos', 'todas', 'tal', 'si', 'no', 'sí', 'creo', 'cómo', 'decía', 'año', 'tema', 'entonces',
                 'claor', 'bueno', 'decir', 'ahora', 'aquí','sé', 'día', 'puede', 'ejemplo', 'claro', 'gente', 'cosa', 'después', 'ver',
                 'eh', 'pues', 'quiero', 'dice', 'cosas', 'momento', 'mucha', 'años', 'mucho', 'muchas', 'muchos', 'bien', 'hecho', 'ser', 'ir',
                 'mejor', 'así', 'gusta', 'alguien', 'hablando', 'ser', 'dices', 'veces', 'siempre', 'persona', 'vale', 'gustaría', 'parece',
                 'menos', 'voy', 'hace', 'hacer', 'depende', 'digamos', 'tampoco', 'va', 'cada', 'mismo', 'digo', 'sido', 'dónde', 'veo',
                 'seguimos', 'da', 'de', 'dé', 'aquel', 'tan', 'mas', 'más']

stop_words_span.update(stopwords_add)

# Transform set into list:
stop_words_span = list(stop_words_span)

vectorizer_model = CountVectorizer(stop_words = stop_words_span)
bert_model = BERTopic(language="spanish", vectorizer_model = vectorizer_model)
topics, ini_probs= bert_model.fit_transform(df['text_cleaned'])

df['num_topic'] = topics

# The distance between informers can be calculated without the topics -1. When we use BERTopic, some topics are assigned to -1 value. 
# That means that these topics are outliers and were not assigned to any important topic.
# So we can delete the rows with -1 topic number and the MOD (moderator) rows:

df_filtered = df.loc[df['num_topic'] != -1]
df_filtered = df_filtered.loc[~df_filtered['informer'].str.contains('MOD')]

# Now we can calculate the vectorization of our documents, transform in df, and concat we the original:

doc_vect = vectorizer_model.fit_transform(df_filtered['text_cleaned'])
df_vect = pd.DataFrame(doc_vect.toarray(), columns=vectorizer_model.get_feature_names_out())

# It is necessary to concat the dataframes. Be careful with the index and check it with df.shape:
df_filtered = df_filtered.reset_index(drop=True)
df_vect = df_vect.reset_index(drop=True)
df_to_distance = pd.concat([df_filtered, df_vect], axis=1)

# Now we will do a visualization to see the distance between informers. 
# There are too many way to do it. I choosed the most easy-way option in this case. 
# I used the vectorization result with CountVectorizer and reduced the dimentionality (to 2 p.components). 
# Then, I calculated the mean of each component and use plotly:

X = df_to_distance.drop(columns = ['informer', 'text', 'text_cleaned', 'text_cleaned_nstopwords', 'num_topico'])
comp_names = ['Comp 1', 'Comp 2']
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(X), columns = comp_names)

df_to_distance = df_to_distance.reset_index(drop=True)
df_pca = df_pca.reset_index(drop=True)
df_to_distance = pd.concat([df_to_distance, df_pca], axis=1)

df_comp_means = df_to_distance.groupby('informer').agg({'Comp 1': 'mean', 'Comp 2': 'mean'}).reset_index()
df_comp_means['size_point'] = 30 # I also added the size of the point in the chart. 

# Sometimes, it is necessary to standarize the data before PCA. In this case, it was not necessary, but it depends on your data. 
# I recommend to make df.describe() and df.info() to be sure about what to do first.

# Now, in order to generate a inter-informer distance graph, we need to know the mean of our components:
mean_comp1_total = df_comp_means['Comp 1'].mean()
mean_comp2_total = df_comp_means['Comp 2'].mean()

# Now we can generate the graph with the mean of Comp 1 and Comp 2 in the middle:

fig = px.scatter(
    df_comp_means,
    x = 'Comp 1',
    y = 'Comp 2',
    color = 'informer',
    size = 'size_point',
    size_max = 25,
    title = 'Distance inter-informer'
)

# Modify the graph position to center it to the mean of the PC:

fig.update_layout(
    xaxis = dict(range = [mean_comp1_total - 0.9, mean_comp1_total + 0.9]),
    yaxis = dict(range = [mean_comp2_total - 0.9, mean_comp2_total + 0.9]),
    title_font=dict(color = 'black'),
    title_x = 0.5,
    title_y = 0.95
)

# Add black lines to the graph:

fig.add_shape(
    type = 'line',
    x0 = mean_comp1_total, y0 = mean_comp2_total - 2,
    x1 = mean_comp1_total, y1 = man_comp2_total + 2,
    line = dict(color = 'black', width = 1)
)

fig.add_shape(
    type = 'line',
    x0 = mean_comp1_total - 2, y0 = mean_comp2_total,
    x1 = mean_comp1_total + 2, y1 = mean_comp2_total,
    line = dict(color = 'black', width = 1)
)

fig.show()
