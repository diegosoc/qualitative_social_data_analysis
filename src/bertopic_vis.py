from sklearn.feature_extraction.text import CountVectorizer

vectorizer_model = CountVectorizer(stop_words=stop_words_esp)
bert_model = BERTopic(language="spanish", vectorizer_model=vectorizer_model)

# Ajustar el modelo a los datos
topics, ini_probs= bert_model.fit_transform(df['text_cleaned'])

bert_model.visualize_barchart(top_n_topics = 16, n_words = 10)

bert_model.visualize_topics()

bert_model.visualize_documents(df['text_cleaned'])

bert_model.visualize_hierarchy()

bert_model.visualize_heatmap()