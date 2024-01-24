import pytest
import zipfile
from src._1_unzip_CL_function import unzip_CL_folder

# Module created to testing the data resource creation:
# The unzip_CL_folder and pdf_to_txt files were having some problems. 
# I created this test to monitorint the function.

class TestUnzipCL:

    @pytest.fixture

    def create_temp_zip_files(self, tmp_path):

        # Create temo dict:
        temp_zip_folder = tmp_path / "studies_temp_folder"
        temp_zip_folder.mkdir()

        # Temp studies numbers:
        study_numbers = [3251, 1234, 5678]

        for study_number in study_numbers:
            zip_file_path = temp_zip_folder / f"{study_number}.zip"
            with zipfile.ZipFile(zip_file_path, "w") as zip_file:
                zip_file.writestr(f"{study_number}_file.txt", "Content")
                
        unzipped_folder = tmp_path / "unzipped_CL_data"

        return temp_zip_folder, study_numbers, unzipped_folder

    def test_unzip_CL_folder(self, create_temp_zip_files):

        zip_folder, study_numbers, unzipped_folder = create_temp_zip_files

        # Test function:
        unzip_CL_folder(zip_folder, study_numbers, unzipped_folder)

        # Verify function is working well:
        for study_number in study_numbers:
            unzipped_file_path = unzipped_folder / f"{study_number}_file.txt"
            assert unzipped_file_path.is_file()

class TestPdfToTxt:

    @pytest.fixture
    def sample_pdf_folder(self, tmp_path):
        # Create a temporary folder with sample PDF files for testing
        pdf_folder = tmp_path / "pdf_temp_folder"
        pdf_folder.mkdir()
        
        # Create a sample PDF file
        sample_pdf_path = pdf_folder / "sample.pdf"
        with open(sample_pdf_path, "w", encoding="utf-8") as sample_pdf:
            sample_pdf.write("Sample PDF content")
        
        return pdf_folder

    def test_pdf_to_txt(self, tmp_path, sample_pdf_folder):
        # Set up the test folders
        input_folder = sample_pdf_folder
        output_folder = tmp_path / "output_txt_folder"

        # Test the pdf_to_txt function
        pdf_to_txt(input_folder, output_folder)

        # Check if the output folder and text files are created
        assert os.path.exists(output_folder)
        
        # Check if a text file is created for each PDF file in the input folder
        for pdf_file in os.listdir(input_folder):
            if pdf_file.lower().endswith(".pdf"):
                txt_file = os.path.join(output_folder, os.path.splitext(pdf_file)[0] + ".txt")
                assert os.path.exists(txt_file)

                # Check if the content of the text file is not empty
                with open(txt_file, "r", encoding="utf-8") as file_txt:
                    content = file_txt.read()
                    assert content.strip() == "Sample PDF content"
