#!/usr/bin/env python3

import os
from pathlib import Path

def organize_downloads(downloads_folder: Path):

    if not downloads_folder.exists():
        print(f"Error: The folder {downloads_folder} does not exist.")
        return
        
    for item in downloads_folder.iterdir():
        # Only process files (skip directories)
        if not item.is_file():
            continue

def main():

    downloads_path = Path(os.path.expanduser("~/Downloads"),)
    organize_downloads(downloads_path)

if __name__ == "__main__":
    main()
