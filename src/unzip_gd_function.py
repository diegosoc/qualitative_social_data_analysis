import os
import zipfile

#You have to provide the folder where you saved the unzipped data from the main CIS zip folders
#You have to provide a new folder for the destination or let the function create one

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

#Example:
unzip_gdmain_folders('qualitative_unzipped_data', 'qlt_unzipped_data_lang_options')