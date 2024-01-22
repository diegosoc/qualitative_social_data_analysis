import os
from pdfminer.high_level import extract_text

def pdf_to_txt(folder_transcriptions: str, folder_transcriptions_txt: str):

    """
    We need to read the transcriptions to work with them in Python. So, first, we need to transform
    the pdf files into txt files. This function transform every single pdf file in the folder provided
    and give us the txt file for each transcription in a new folder. 
    
    """
    if not os.path.exists(folder_transcriptions_txt):
        os.makedirs(folder_transcriptions_txt)
    file_pdf = [
        file
        for file in os.listdir(folder_transcriptions)
        if file.lower().endswith(".pdf")
    ]

    for file_pdf in file_pdf:
        path_pdf = os.path.join(folder_transcriptions, file_pdf)
        path_txt = os.path.join(
            folder_transcriptions_txt, os.path.splitext(file_pdf)[0] + ".txt"
        )
        text = extract_text(path_pdf)

        with open(path_txt, "w", encoding="utf-8") as file_txt:
            file_txt.write(text)


# Example of use: pdf_to_txt("data/unzipped_LANG_data", "data/transcriptions_txt_folder")
