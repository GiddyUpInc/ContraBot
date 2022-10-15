"""
Description:
    File contains miscellaneous utility functions
"""

import os

# Functions for string handling

def get_filename(path: str):
    """Return the filename with no path or extension"""
    pass

def get_extension(filename: str):
    """Return file extension"""
    pass

def get_dir(path: str):
    """Remove filename from path to file and return"""
    pass

# Functions for parsing directories

def list_wav_files(dir: str):
    output = []
    items = os.listdir(dir)

    for item in items:
        if item.split('.')[1] == "wav":
            output.append(item)

    return output