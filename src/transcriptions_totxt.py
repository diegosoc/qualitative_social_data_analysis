import os
from pdfminer.high_level import extract_text
import re

def pdf_to_txt(folder_transcriptions: str, folder_transcriptions_txt: str) -> Processed files:
    if not os.path.exists(folder_transcriptions_txt):
        os.makedirs(folder_transcriptions_txt)
    file_pdf = [file for file in os.listdir(folder_transcriptions) if file.lower().endswith('.pdf')]

    for file_pdf in file_pdf:
        path_pdf = os.path.join(folder_transcriptions, file_pdf)
        path_txt = os.path.join(folder_transcriptions_txt, os.path.splitext(file_pdf)[0] + '.txt')
        text = extract_text(path_pdf)

        with open(path_txt, "w", encoding='utf-8') as file_txt:
            file_txt.write(text)

pdf_to_txt('unziped_data3', 'unziped_data4')
