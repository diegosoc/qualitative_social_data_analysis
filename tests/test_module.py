
import os
import pandas as pd
import pytest
import shutil
import zipfile
from src._4_pdf_to_txt_function import pdf_to_txt
from src._1_unzip_CL_function import unzip_CL_folder

# Module created to testing the data resource creation:
# The unzip_CL_folder was having problems, so I created this test to monitorint the function:

class TestUnzipCL:

    @pytest.fixture

    def create_temp_zip_files(self, tmp_path):

        # Crear archivos zip de prueba en un directorio temporal
        temp_zip_folder = tmp_path / "studies_temp_folder"
        temp_zip_folder.mkdir()

        # Nombres de estudio de prueba
        study_numbers = [3251, 1234, 5678]

        for study_number in study_numbers:
            zip_file_path = temp_zip_folder / f"{study_number}.zip"
            with zipfile.ZipFile(zip_file_path, "w") as zip_file:
                zip_file.writestr(f"{study_number}_file.txt", "Content")

        # Directorio de destino para la descompresión
        unzipped_folder = tmp_path / "unzipped_CL_data"

        return temp_zip_folder, study_numbers, unzipped_folder

    def test_unzip_CL_folder(self, create_temp_zip_files):

        zip_folder, study_numbers, unzipped_folder = create_temp_zip_files

        # Ejecutar la función bajo prueba
        unzip_CL_folder(zip_folder, study_numbers, unzipped_folder)

        # Verificar que los archivos se han descomprimido correctamente
        for study_number in study_numbers:
            unzipped_file_path = unzipped_folder / f"{study_number}_file.txt"
            assert unzipped_file_path.is_file()