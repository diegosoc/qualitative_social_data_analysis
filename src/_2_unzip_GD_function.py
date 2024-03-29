import os
import zipfile

def unzip_gd_folders(folder_with_CL_unzipped_data: str, unzipped_gd_files_folder: str):

    """ 
    This function unzip the zip file (with the information about the
    discusion group - GD -) in the folder which contains the last unzip files
    from the first unzip function.
    
    """
    if not os.path.exists(folder_with_CL_unzipped_data):
        print(f"The folder named {folder_with_CL_unzipped_data} does not exist")
    if not os.path.exists(unzipped_gd_files_folder):
        os.makedirs(unzipped_gd_files_folder)
    files = os.listdir(folder_with_CL_unzipped_data)
    for file in files:
        file_path = os.path.join(folder_with_CL_unzipped_data, file)
        if file_path.endswith("zip"):
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(os.path.join(unzipped_gd_files_folder))


# Example of use: unzip_gd_folders("data/unzipped_CL_data", "data/unzipped_GD_data")
