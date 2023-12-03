import os
import zipfile

def unzip_gdmain_folders(folder_with_unzipped_data, unziped_gd_files_folder):
    if not os.path.exists(folder_with_unzipped_data):
        print(f'The folder named {folder_with_unzipped_data} does not exist')
    if not os.path.exists(unziped_gd_files_folder):
        os.makedirs(unziped_gd_files_folder)
    files = os.listdir(folder_with_unzipped_data)
    for file in files:
        file_path = os.path.join(folder_with_unzipped_data, file)
        if file_path.endswith('zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.join(unziped_gd_files_folder))

