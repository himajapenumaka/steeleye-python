import xml.etree.ElementTree as ET
import requests
from zipfile import ZipFile
import os

# Read the XML file.
tree = ET.parse('select.xml')
root = tree.getroot()

# Find the download link for DLTINS.
for doc in root.iter('doc'):
    file_type = doc.find('str[@name="file_type"]').text
    if file_type == 'DLTINS':
        download_link = doc.find('str[@name="download_link"]').text
        break

# Download the ZIP file.
response = requests.get(download_link)
with open('zip_file.zip', 'wb') as f:
    f.write(response.content)

if not os.path.exists("zip_file"):
    os.mkdir("zip_file")

# Extract the XML file from the ZIP.
with ZipFile("zip_file.zip", 'r') as zip_object:
    zip_object.extractall(path="zip_file")