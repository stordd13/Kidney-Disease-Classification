import zipfile
from pathlib import Path

zipfile_path = "artifacts/data_ingestion/data.zip"

with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
    zip_ref.extractall("artifacts/data_ingestion")