
import os
import pandas as pd
import pytest
import shutil
import zipfile
from src._4_pdf_to_txt_function import pdf_to_txt
from src._1_unzip_CL_function import unzip_CL_folder

# Module created to testing the data resource creation:

class UnzipCL:

    @pytest.fixture

    def create_temp_zip_files(tmp_path):

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

    def test_unzip_CL_folder(create_temp_zip_files):

        zip_folder, study_numbers, unzipped_folder = create_temp_zip_files()

        # Ejecutar la función bajo prueba
        unzip_CL_folder(zip_folder, study_numbers, unzipped_folder)

        # Verificar que los archivos se han descomprimido correctamente
        for study_number in study_numbers:
            unzipped_file_path = unzipped_folder / f"{study_number}_file.txt"
            assert unzipped_file_path.is_file()

class UnzipGD:

    @pytest.fixture

    def test_data(tmp_path):

        # Create a temporary folder with test data
        folder_with_CL_unzipped_data = os.path.join(tmp_path, "data/unzipped_CL_data")
        unzipped_gd_files_folder = os.path.join(tmp_path, "data/unzipped_GD_data")

        os.makedirs(folder_with_CL_unzipped_data)
        os.makedirs(unzipped_gd_files_folder)

        # Create a test zip file
        zip_file_path = os.path.join(folder_with_CL_unzipped_data, "test.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zip_ref:
            zip_ref.write(os.path.join(folder_with_CL_unzipped_data, "test.txt"), "test.txt")

        return folder_with_CL_unzipped_data, unzipped_gd_files_folder

    def test_unzip_gd_folders(test_data):
        
        folder_with_CL_unzipped_data, unzipped_gd_files_folder = test_data

        # Call the function
        unzip_gd_folders(folder_with_CL_unzipped_data, unzipped_gd_files_folder)

        # Assert that the files were extracted
        assert os.path.exists(unzipped_gd_files_folder)
        assert os.path.exists(os.path.join(unzipped_gd_files_folder, "test.txt"))

        # Clean up test data
        shutil.rmtree(folder_with_CL_unzipped_data)
        shutil.rmtree(unzipped_gd_files_folder)

class UnzipLANG:

    @pytest.fixture
    
    def test_data(tmp_path):
        
        # Create a temporary folder with test data
        folder_with_lang_options = os.path.join(tmp_path, "data/unzipped_GD_data")
        transcriptions_folder = os.path.join(tmp_path, "data/unzipped_LANG_data")

        os.makedirs(folder_with_lang_options)
        os.makedirs(transcriptions_folder)

        # Create a test zip file for Spanish ("castellano")
        zip_file_path = os.path.join(folder_with_lang_options, "test_castellano.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zip_ref:
            zip_ref.write(os.path.join(folder_with_lang_options, "test.pdf"), "test.pdf")

        return folder_with_lang_options, "castellano", transcriptions_folder

    def test_unzip_lang_folder(test_data):
        
        folder_with_lang_options, lang, transcriptions_folder = test_data

        # Call the function
        unzip_lang_folder(folder_with_lang_options, lang, transcriptions_folder)

        # Assert that the files were extracted
        assert os.path.exists(transcriptions_folder)
        assert os.path.exists(os.path.join(transcriptions_folder, "test.pdf"))

        # Clean up test data
        shutil.rmtree(folder_with_lang_options)
        shutil.rmtree(transcriptions_folder)

class TestPdfToTxt:

    def test_pdf_to_txt_files(self, tmp_path):

        # Temporary folder for pdf files:
        pdf_folder = tmp_path / "pdf"
        pdf_folder.mkdir()

        # Create some pdf files:
        for i in range(1, 6):
            pdf_file = pdf_folder / f"file_{i}.pdf"
            pdf_file.touch()

        # Create a temporary folder for txt files:
        txt_folder = tmp_path / "txt"

        # Start the main function:
        pdf_to_txt(pdf_folder, txt_folder)

        # Verify the new folder has the same files as the pdf folder:
        pdf_files = set(os.path.splitext(file)[0] for file in os.listdir(pdf_folder))
        txt_files = set(os.path.splitext(file)[0] for file in os.listdir(txt_folder))

        assert txt_files == pdf_files

class TestTexttoCSV:

    @pytest.fixture

    def test_data(tmp_path):

        # Create a temporary folder with test data
        txt_files_folder = os.path.join(tmp_path, "data/transcription_txt_ed_folder")
        output_folder = os.path.join(tmp_path, "data/dataframes_folder")

        os.makedirs(txt_files_folder)
        os.makedirs(output_folder)

        # Create a test txt file
        txt_file_path = os.path.join(txt_files_folder, "test.txt")
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write("M1: First informer text\nMOD: Moderator text\nH1: Second informer text")

        return txt_files_folder, output_folder

    def test_process_txt_files_folder(test_data):
        
        txt_files_folder, output_folder = test_data

        # Call the function
        process_txt_files_folder(txt_files_folder, output_folder)

        # Assert that the CSV file was created
        assert os.path.exists(output_folder)
        csv_file_path = os.path.join(output_folder, "test.csv")
        assert os.path.exists(csv_file_path)

        # Read the CSV file and assert its content
        df = pd.read_csv(csv_file_path)
        assert "informer" in df.columns
        assert "text" in df.columns
        assert len(df) == 3  # Three paragraphs in the test file

        # Clean up test data
        shutil.rmtree(txt_files_folder)
        shutil.rmtree(output_folder)