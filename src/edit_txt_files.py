import re
import os 

def procesar_archivos_en_carpeta(carpeta):
    # Obtener la lista de archivos en la carpeta
    archivos = [f for f in os.listdir(carpeta) if f.endswith('.txt')]

    # Iterar sobre cada archivo
    for archivo in archivos:
        filename = os.path.join(carpeta, archivo)

        # Read the content of the file

        with open(filename, 'r', encoding = 'utf-8') as file:
            content = file.read()

        # Split the content into paragraphs
        paragraphs = re.split(r'(\n\s*\n)', content)

        # Process each paragraph
        for i in range(0, len(paragraphs), 2):
            paragraph = paragraphs[i]
            if not any(c.islower() for c in paragraph):
                paragraphs[i] = f'MOD: {paragraph.lstrip()}'

        # Join the modified paragraphs back together
        modified_content = ''.join(paragraphs)

        # Write the modified content back to the file
        with open(filename, 'w', encoding = 'utf-8') as file:
            file.write(modified_content)

        with open(filename, 'r', encoding = 'utf-8') as file:
            content = file.read()

        content = re.sub(r'^.*?\[Presentación inicial\].*?(\n|$)', '', content, flags=re.DOTALL)

        # Use regular expressions to remove paragraphs starting with '*'
        content = re.sub(r'\*.*?(\n\n|\n$)', '', content, flags=re.DOTALL)

        # Use regular expressions to remove lines with just numbers
        content = re.sub(r'\b\d+\b', '', content)

        content = re.sub(r'\x0C.*?(\n|$)', '', content, flags=re.DOTALL)

        # Eliminate lines starting with '(' and all lines until a line ending with ')'
        content = re.sub(r'\(.*?\).*?(\n|$)', '', content, flags=re.DOTALL)

        # Ensure at most one empty line between non-empty lines
        content = re.sub(r'(\n\s*){2,}', r'\n\n', content)

        # Remove lines that only contain 'MOD :'
        content = re.sub(r'^\s*MOD\s*:\s*\n', '', content, flags=re.MULTILINE)

        # Add a newline before 'MOD :' if it's not at the beginning of a line
        content = re.sub(r'(?<!\n)MOD:', '\nMOD:', content)

        #Remove extra empty lines
        content = content.replace('\n\n', '\n')

        # Add a newline before 'MOD :' or 'MX:' if it's not at the beginning of a line
        content = re.sub(r'(?<!\n)(MOD:|M\d+:|H\d+:)', r'\n\1', content)

        # Add a newline before 'MOD :' or 'MX:' if it's not at the beginning of a line
        content = re.sub(r'\n(MOD:|M\d+:|H\d+:)', r'\n\n\1', content)

        # Write the modified content back to the file
        with open(filename, 'w', encoding = 'utf-8') as file:
            file.write(content)

        # Read and print the modified content
        with open(filename, 'r', encoding = 'utf-8') as file:
            modified_content = file.read()

procesar_archivos_en_carpeta('unziped_data4')