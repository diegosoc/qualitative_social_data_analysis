import os
import zipfile

#folder : You have to provide folder with zip file is
#study_n : You have to provide a list of strings with the studies you are interested in (list = ['325','234'])
#unziped_files_folder : You have to provide folder where the files will be unzipped or create new one

import os
import zipfile

def unzip_data(folder, studies_list, unziped_files_folder):
    if not os.path.exists(folder):
        print(f'The folder named {folder} does not exist')
        return
    if not os.path.exists(unziped_files_folder):
        os.makedirs(unziped_files_folder)
    files = os.listdir(folder)
    file_paths = []
    files_to_unzip = []
    for file in files:
        file_path = os.path.join(folder, file)
        file_paths.append(file_path)
    for file_path in file_paths:
        if file_path.endswith('.zip'):
            files_to_unzip.append(file_path)
    for file in files_to_unzip:
        if any(str(study) in file for study in studies_list):
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(unziped_files_folder)
            print(f"Se ha descomprimido {file} en {unziped_files_folder}")

#Example:
unzip_data('qualitative_zipped_data', ['325'], 'qualitative_unzipped_data')