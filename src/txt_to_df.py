import os
import pandas as pd
import re

# Función para procesar el archivo y extraer datos
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    texts = []
    informer = ""
    mod = ""

    # Separar por participantes o el moderador
    paragraphs = re.split(r'(M\d+:|MOD:)', content)
    
    # Inicializar variables para mantener el estado
    for par in paragraphs:
        if par.startswith('M'):
            informer = par.strip(':').strip()
        elif par.startswith('MOD'):
            mod = par.strip(':').strip()
        elif informer and par.strip():
            text = par.strip()
            texts.append((informer, text, mod))

    return texts

def process_txtfiles_folder(input_folder, output_folder):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_folder, file_name)
            
            # Procesar el archivo y crear el DataFrame
            txt_df = pd.DataFrame(process_file(file_path), columns=["informer", "text", "mod"])

            # Guardar el DataFrame como un archivo CSV en la carpeta de salida
            output_file_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}.csv')
            txt_df.to_csv(output_file_path, index=False)

# Ejemplo de uso
input_folder = 'carpeta_de_entrada'  # Reemplaza con la carpeta real de tus archivos txt
output_folder = 'carpeta_de_salida'  # Reemplaza con la carpeta donde deseas guardar los CSV
process_txtfiles_folder('unziped_data4', 'gd1')