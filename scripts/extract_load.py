import zipfile
import os

# Path to the uploaded zip file
zip_file_path = 'data/archive.zip'
extracted_folder_path = 'data/extracted'

# Create a directory to extract the files
os.makedirs(extracted_folder_path, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# List the extracted files
extracted_files = os.listdir(extracted_folder_path)
extracted_files
