import os
from pdfminer.high_level import extract_text

def convertir_pdf_a_txt_en_carpeta(transcriptions, transcriptionstxt):
    # Verifica si la carpeta de destino existe, y si no, créala
    if not os.path.exists(transcriptionstxt):
        os.makedirs(transcriptionstxt)

    # Lista todos los archivos en la carpeta de origen
    archivos_pdf = [archivo for archivo in os.listdir(transcriptions) if archivo.lower().endswith('.pdf')]

    for archivo_pdf in archivos_pdf:
        # Construye las rutas completas para el archivo de origen y el archivo de destino
        ruta_pdf = os.path.join(transcriptions, archivo_pdf)
        ruta_txt = os.path.join(transcriptionstxt, os.path.splitext(archivo_pdf)[0] + '.txt')

        # Extrae el texto del archivo PDF
        texto = extract_text(ruta_pdf)

        # Abre el archivo de texto en modo de escritura ('w' para sobrescribir)
        with open(ruta_txt, "w", encoding='utf-8') as file_txt:
            # Escribe el texto en el archivo de texto
            file_txt.write(texto)

# Reemplaza 'ruta/a/carpeta_origen' con la ruta de tu carpeta de origen
# Reemplaza 'ruta/a/carpeta_destino' con la ruta de la carpeta donde quieres guardar los archivos de texto
convertir_pdf_a_txt_en_carpeta('transcriptions', 'transcriptionstxt')
