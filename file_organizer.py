#!/usr/bin/env python3

import os
from pathlib import Path
from datetime import datetime

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

def main():

    downloads_path = Path(os.path.expanduser("~/Downloads"),)
    organize_downloads(downloads_path)

if __name__ == "__main__":
    main()
