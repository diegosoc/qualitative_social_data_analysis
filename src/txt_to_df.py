import pandas as pd
import re

def txt_to_df (file_path):

    with open(file_path, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    texts = contenido.split('\n\n')

    texts_with_M = [text.strip() for text in texts if text.startswith('M') and text[1].isdigit()]

    df = pd.DataFrame(texts_with_M, columns=['text'])

    df['informer'] = df['text'].apply(lambda x: re.search(r'M\d', x).group() if re.search(r'M\d', x) else '')

    df['text'] = df['text'].apply(lambda x: re.sub(r'M\d', '', x).strip())

    return df