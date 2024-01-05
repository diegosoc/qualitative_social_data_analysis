import os
import zipfile

# It is necessary to create a function to unzip the first CIS folder that appears when we download the study information (CL folder):

def unzip_CL_folder (studies_folder: str, studies_list: list, unzipped_files_folder: str):
    if not os.path.exists(studies_folder):
        print(f'The folder named {studies_folder} does not exist')
        return
    if not os.path.exists(unzipped_files_folder):
        os.makedirs(unzipped_files_folder)
    folders = os.listdir(studies_folder)
    folder_paths = []
    folders_to_unzip = []
    for folder in folders:
        folder_path = os.path.join(studies_folder, folder)
        folder_paths.append(folder_path)
    for folder_path in folder_paths:
        if folder_path.endswith('.zip'):
            folders_to_unzip.append(folder_path)
    for folder in folders_to_unzip:
        if any(str(study) in folder for study in studies_list):
            with zipfile.ZipFile(folder, 'r') as zip_ref:
                zip_ref.extractall(unzipped_files_folder)
            print(f"{folder} has been unzipped in {unzipped_files_folder}")

# Example of usage:
# unzip_CL_folder ('studies_folder', [3251], 'unzipped_CL_data')
