# APPLYING THE CODE TO THE CIS STUDY 3251:
# STUDY TITLE: "ESTUDIO CUALITATIVO SOBRE EL PROCÉS DE INDEPENDENCIA EN CATALUÑA (2018)
# TRANSCRIPTIONS E3251_GD04

from _1_unzip_CL_function import unzip_CL_folder
from _2_unzip_GD_function import unzip_gd_folders
from _3_unzip_LANG_function import unzip_lang_folder
from _4_transcriptions_to_txt_function import pdf_to_txt
from _5_edit_transcriptions_txt_function import process_file_in_folder
from _6_txt_to_df_function import process_file, process_txt_files_folder

unzip_CL_folder ('studies_folder', [3251], 'unzipped_CL_data')
unzip_gd_folders ('unzipped_CL_data', 'unzipped_GD_data')
unzip_lang_folder ('unzipped_GD_data', 'castellano', 'unzipped_LANG_data')
pdf_to_txt ('unzipped_LANG_data', 'transcriptions_txt_folder')
process_file_in_folder ('transcriptions_txt_folder', 'transcription_txt_ed_folder')
process_txt_files_folder ('transcription_txt_ed_folder', 'dataframes_folder')

#NEXT STEPS:
# 1. WORDCLOUD TO AS FIRST STEP TO EXPLORE THE QUALITATIVE DATA
# 2. MAIN TERMS WITH TF-IDF
# 3. TOPIC ANALYSIS WITH BERTOPIC
# 4. INTERDISTANCE BETWEEN INFORMERS
# 5. MAKE SOME VISUALIZATION LIKE IN TIME_INFORMER_SPEAK FILE