from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

#We can use CountVectorizer or other tool to get the embeddings. In this case I used CountVectorizer:
vectorizer_model = CountVectorizer(stop_words=stop_words_esp)
bert_model = BERTopic(language="spanish", vectorizer_model=vectorizer_model)

# Fit the model to our data:
topics, ini_probs= bert_model.fit_transform(df['text_cleaned'])

#Visualization of bertopic results:
#1. Barchart with topics and probabilities:
bert_model.visualize_barchart(top_n_topics = 16, n_words = 10)
#2. Intertopic distance map:
bert_model.visualize_topics()
#3. Visualization of the topic-clusters:
bert_model.visualize_documents(df['text_cleaned'])
#4. Hierarchical clustering of topics:
bert_model.visualize_hierarchy()
#5. Similarity information (matrix) of the topics:
bert_model.visualize_heatmap()
