import os
from pdfminer.high_level import extract_text

def convertir_pdf_a_txt_en_carpeta(transcriptions, transcriptionstxt):
    if not os.path.exists(transcriptionstxt):
        os.makedirs(transcriptionstxt)
    archivos_pdf = [archivo for archivo in os.listdir(transcriptions) if archivo.lower().endswith('.pdf')]

    for archivo_pdf in archivos_pdf:
        ruta_pdf = os.path.join(transcriptions, archivo_pdf)
        ruta_txt = os.path.join(transcriptionstxt, os.path.splitext(archivo_pdf)[0] + '.txt')
        texto = extract_text(ruta_pdf)

        with open(ruta_txt, "w", encoding='utf-8') as file_txt:
            # Escribe el texto en el archivo de texto
            file_txt.write(texto)
