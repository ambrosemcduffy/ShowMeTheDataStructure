"""
This module find files
for a given suffix path
"""
import os


path = "./"

def find_files(suffix,  path) -> list:
    print("...Searching Directory...\n")
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
                print(file_path)
                file_paths.append(file_path)
            if os.path.isdir(new_path):
                parse_folder(index-1, suffix, new_path)
    parse_folder(index_n, suffix, path)
    if len(file_paths) == 0:
        print("File paths does not exist..")
    return file_paths


file_paths = find_files(".h", path)
