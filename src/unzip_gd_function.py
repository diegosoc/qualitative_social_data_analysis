import os
import zipfile

# Once the CL folder is unziped (unzip_function.py), it is necessary to unzip another folder (GD{study code}).

def unzip_gd_folders(folder_with_unzipped_data: str, unziped_gd_files_folder: str) -> folder:
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

# Example of usage:
# unzip_gd_folders('unziped_data', 'unziped_data2')
