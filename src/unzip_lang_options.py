import os
import zipfile


def unzip_gd_for_transcriptions(folder_with_lang_options, lang, transcriptions_folder):
    if not os.path.exists(folder_with_lang_options):
        print(f'The folder named {folder_with_lang_options} does not exist')
    if not os.path.exists(transcriptions_folder):
        os.makedirs(transcriptions_folder)
    files = os.listdir(folder_with_lang_options)
    for file in files:
        file_path = os.path.join(folder_with_lang_options, file)
        if lang in file_path and file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.join(transcriptions_folder))

unzip_gd_for_transcriptions('unziped_data2', 'castellano', 'unziped_data3')
