import os
import pandas as pd
import re

# It is necessary to create a functions to transform the text fles into dataframes.
# These files weill be saved as CSV files in a folder to be used in any time.


# 1. Function to create
def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        texts = []
        informer = ""
        mod = ""

    # Split paragraphs from informers (M1, M2... H1, H2...) or moderator (MOD):
    paragraphs = re.split(r"(M\d+:|MOD:|H\d+:)", content)

    # Find the paragraphs:
    for par in paragraphs:
        if par.startswith("M"):
            informer = par.strip(":").strip()
        elif par.startswith("H"):
            informer = par.strip(":").strip()
        elif par.startswith("MOD"):
            mod = par.strip(":").strip()
        elif informer and par.strip():
            text = par.strip()
            texts.append((informer, text))
    return texts


# 2. Function to process the files transforming them into dataframes and save them as CSV files:
def process_txt_files_folder(txt_files_folder: str, output_folder: str):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(txt_files_folder):
        if file_name.endswith(".txt"):
            file_path = os.path.join(txt_files_folder, file_name)

            # Pocess the file and create the dataframe
            txt_df = pd.DataFrame(process_file(file_path), columns=["informer", "text"])

            # Save the dataframe into CSV file:
            output_file_path = os.path.join(
                output_folder, f"{os.path.splitext(file_name)[0]}.csv"
            )
            txt_df.to_csv(output_file_path, index=False)


# Usage examle:
process_txt_files_folder("transcription_txt_ed_folder", "dataframes_folder")
