import re
import os 

#It is necessary to create a function to process the text files in order to get ready to transform in a Dataframe and work with it:
#This step depends on the style of the CIS documents, I took the example of the most recent studies, but it could be different:

def process_file_in_folder (folder_transcriptions_txt: str, transcription_txt_ed_folder: str):
    
    # Get a list with the files in folder:
    files = [f for f in os.listdir(folder_transcriptions_txt) if f.endswith('.txt')]

    if not os.path.exists(transcription_txt_ed_folder):
        os.makedirs(transcription_txt_ed_folder)

    # Get the full filenames with the path:
    for file in files:
        input_file = os.path.join(folder_transcriptions_txt, file)
        output_file = os.path.join(transcription_txt_ed_folder, file)

        # Read the content of each file:
        with open(input_file, 'r', encoding = 'utf-8') as file:
            content = file.read()

        # Split the content into paragraphs using regular expresions:
        paragraphs = re.split(r'(\n\s*\n)', content)

        #Process each paragraph:
        for i in range(0, len(paragraphs), 2):
            paragraph = paragraphs[i]
            if not any(c.islower() for c in paragraph):
                paragraphs[i] = f'MOD: {paragraph.lstrip()}'

        # Join the modified paragraphs back together
        modified_content = ''.join(paragraphs)

        # Eliminate from the start to [Presentación inicial]
        modified_content = re.sub(r'^.*?\[Presentación inicial\].*?(\n|$)', '', modified_content, flags=re.DOTALL)

        # Use regular expressions to remove paragraphs starting with '*'
        modified_content = re.sub(r'\*.*?(\n\n|\n$)', '', modified_content, flags=re.DOTALL)

        # Use regular expressions to remove lines with just numbers
        modified_content = re.sub(r'\b\d+\b', '', modified_content)

        modified_content = re.sub(r'\x0C.*?(\n|$)', '', modified_content, flags=re.DOTALL)

        # Eliminate lines starting with '(' and all lines until a line ending with ')'
        modified_content = re.sub(r'\(.*?\).*?(\n|$)', '', modified_content, flags=re.DOTALL)

        # Ensure at most one empty line between non-empty lines
        modified_content = re.sub(r'(\n\s*){2,}', r'\n\n', modified_content)

        # Remove lines that only contain 'MOD :'
        modified_content = re.sub(r'^\s*MOD\s*:\s*\n', '', modified_content, flags=re.MULTILINE)

        # Add a newline before 'MOD :' if it's not at the beginning of a line
        modified_content = re.sub(r'(?<!\n)MOD:', '\nMOD:', modified_content)

        #Remove extra empty lines
        modified_content = modified_content.replace('\n\n', '\n')

        # Add a newline before 'MOD :' or 'MX:' if it's not at the beginning of a line
        modified_content = re.sub(r'(?<!\n)(MOD:|M\d+:|H\d+:)', r'\n\1', modified_content)

        # Add a newline before 'MOD :' or 'MX:' if it's not at the beginning of a line
        modified_content = re.sub(r'\n(MOD:|M\d+:|H\d+:)', r'\n\n\1', modified_content)

        #Modification added to correct errors of the first correction:

        modified_content = re.sub(r'(?i)^.*?\[Presentación\sInicial\].*?(\n|$)', '', modified_content, flags=re.DOTALL)

        modified_content = re.sub(r'(?i)^.*?\[Presentació\sInicial\].*?(\n|$)', '', modified_content, flags=re.DOTALL)

        # Write the modified content back to the file
        with open(output_file, 'w', encoding = 'utf-8') as file:
            file.write(modified_content)

process_file_in_folder ('transcriptions_txt_folder', 'transcription_txt_ed_folder')
