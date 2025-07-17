import zipfile
import os

'''
#zip two files to a pubmed.zip file
file_to_zip = ['./src/pubmed/pubmed.py', './src/pubmed/__main__.py']
zip_path = './zip/pubmed.zip'

try:
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in file_to_zip:
            #zipf.write(file, arcname = 'pubmedzp')
            zipf.write(file, arcname=os.path.basename(file))
    print(f"file zipped successfully at {zip_path}")

except IOError as e:
    print(f"an error occurred while zipping a file:{e}")

'''
#unzip all files in a zip archive
arc_zip_path = './zip/pubmed.zip'
output_directory = './unzip'

try:
    with zipfile.ZipFile(arc_zip_path, 'r') as zipf:
        zipf.extractall(output_directory)
except IOError as e:
    print(f"an error occurred while unzip a file:{e}")
    