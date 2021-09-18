"""
This module find files
for a given suffix path
"""
import os


path = "./"

def find_files(suffix,  path) -> list:
    """ Parse folder structure and find files
    Args:
        suffix (str): string of suffix
        path (str): string path
    Returns:
        list: list of string file paths
    """
    
    if suffix == " " or path == " ":
        print("\n---No path input---")
        return " "

    elif suffix is None or path is None:
        print("\n---Null values input---")
        return None

    else:
        print("\n...Searching Directory...\n")

    index_n = len(os.listdir(path))
    file_paths = []

    def parse_folder(index, suffix, path):
        if index <= 0:
            return path

        dir_l = os.listdir(path)

        for files in dir_l:
            new_path = os.path.join(path, files)

            if new_path.endswith(suffix):
                file_path = new_path
                file_paths.append(file_path)
            
            if os.path.isdir(new_path):
                parse_folder(index-1, suffix, new_path)
    
    parse_folder(index_n, suffix, path)
    
    if len(file_paths) == 0:
        print("File paths does not exist..")
    
    return file_paths

# Unit Test 1
# Expecting file path .h
file_paths = find_files(".h", path)
print(file_paths)

# Unit Test 2
# Expecting file path .c
file_paths = find_files(".c", path)
print(file_paths)

# Unit Test 3
# Expecting empty
file_paths = find_files(" ", " ")
print(file_paths)

# Unit Test 4
# Expecting None
file_paths = find_files(None, None)
print(file_paths)