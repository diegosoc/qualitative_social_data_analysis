import os
from pdfminer.high_level import extract_text
import re

def pdf_to_txt(transcriptions, transcriptionstxt):
    if not os.path.exists(transcriptionstxt):
        os.makedirs(transcriptionstxt)
    file_pdf = [file for file in os.listdir(transcriptions) if file.lower().endswith('.pdf')]

    for file_pdf in file_pdf:
        path_pdf = os.path.join(transcriptions, file_pdf)
        path_txt = os.path.join(transcriptionstxt, os.path.splitext(file_pdf)[0] + '.txt')
        text = extract_text(path_pdf)

        with open(path_txt, "w", encoding='utf-8') as file_txt:
            file_txt.write(text)

pdf_to_txt('transcriptions', 'textitos')