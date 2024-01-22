import os
import zipfile

def unzip_lang_folder(
    folder_with_lang_options: str, lang: str, transcriptions_folder: str
):
    """
    Once the zip file with the information of the discusion group is unzipped (unzip_gd_function.py) 
    it is necessary to unzip another file. The file that will be unzipped depends on what we are looking for.
    In this case, if we need to work with the spanish transcriptions, we need to unzip the "castellano" file.
    With this function a new folder will be created with the transcriptions of the discusion groups
    in pdf format.
    
    """
    if not os.path.exists(folder_with_lang_options):
        print(f"The folder named {folder_with_lang_options} does not exist")
    if not os.path.exists(transcriptions_folder):
        os.makedirs(transcriptions_folder)
    files = os.listdir(folder_with_lang_options)
    for file in files:
        file_path = os.path.join(folder_with_lang_options, file)
        if lang in file_path and file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(os.path.join(transcriptions_folder))


# Example of use: unzip_lang_folder("data/unzipped_GD_data", "castellano", "data/unzipped_LANG_data")
