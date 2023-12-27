import os
import pandas as pd
import re

# It is necessary to create a functions to transform the text fles into dataframes.
# These files weill be saved as CSV files in a folder to be used in any time.

# 1. Function to create 
def process_file(file_path: Path) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        texts = []
        informer = ""
        mod = ""

    # Split paragraphs from informers (M1, M2... H1, H2...) or moderator (MOD):
    paragraphs = re.split(r'(M\d+:|MOD:|H\d+:)', content)
    
    # Find the paragraphs:
    for par in paragraphs:
        if par.startswith('M'):
            informer = par.strip(':').strip()
        elif par.startswith('H'):
            mod = par.strip(':').strip()
        elif par.startswith('MOD'):
            mod = par.strip(':').strip()
        elif informer and par.strip():
            text = par.strip()
            texts.append((informer, text, mod))
    return texts

# 2. Function to process the files transforming them into dataframes and save them as CSV files:
def process_txtfiles_folder(input_folder: str, output_folder: str) -> Processed files:
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_folder, file_name)
            
            # Pocess the file and create the dataframe
            txt_df = pd.DataFrame(process_file(file_path), columns=["informer", "text", "mod"])

            # Save the dataframe into CSV file:
            output_file_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}.csv')
            txt_df.to_csv(output_file_path, index=False)

# Usage examle:
#input_folder = 'carpeta_de_entrada'
#output_folder = 'carpeta_de_salida'

#process_txtfiles_folder('unziped_data4', 'gd1')
