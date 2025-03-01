#!/usr/bin/env python3

import os
from pathlib import Path
from datetime import datetime

FILE_TYPE_MAPPING = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
    'pdfs': ['pdf'],
    'documents': ['doc', 'docx', 'txt', 'odt', 'rtf', 'md'],
    'spreadsheets': ['xls', 'xlsx', 'csv'],
    'presentations': ['ppt', 'pptx'],
    'videos': ['mp4', 'avi', 'mov', 'mkv', 'wmv'],
    'audio': ['mp3', 'wav', 'flac', 'aac'],
    'archives': ['zip', 'rar', 'tar', 'gz', '7z']
}

def get_category(extension):

    ext = extension.lower().lstrip('.')
    for category, extensions in FILE_TYPE_MAPPING.items():
        if ext in extensions:
            return category
    return "others"

def organize_downloads(downloads_folder: Path):

    if not downloads_folder.exists():
        print(f"Error: The folder {downloads_folder} does not exist.")
        return
        
    for item in downloads_folder.iterdir():
        # Only process files (skip directories)
        if not item.is_file():
            continue
    
        mod_time = datetime.fromtimestamp(item.stat().st_mtime)
        month = mod_time.strftime("%B")
        year = mod_time.strftime("%Y")
        # Create a folder name that includes both month and year.
        dir_name = f"{month} {year}"
        month_dir = downloads_folder / dir_name
        month_dir.mkdir()
        category = get_category(item.suffix)



def main():

    downloads_path = Path(os.path.expanduser("~/Downloads"),)
    organize_downloads(downloads_path)

if __name__ == "__main__":
    main()
