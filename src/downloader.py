"""
Helpers for downloading files (PDFs etc.).
"""
import os
import requests
from .config import DOWNLOAD_DIR, REQUEST_TIMEOUT

os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_file(url, out_folder=None):
    out_folder = out_folder or DOWNLOAD_DIR
    os.makedirs(out_folder, exist_ok=True)
    local_filename = os.path.join(out_folder, os.path.basename(url.split("?")[0]))
    with requests.get(url, stream=True, timeout=REQUEST_TIMEOUT) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename
