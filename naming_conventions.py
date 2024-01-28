import os
import json

def create_blank_notebook(name):
    """Create a blank Jupyter notebook with the given name."""
    notebook_structure = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 4
    }
    with open(name, 'w', encoding='utf-8') as notebook_file:
        json.dump(notebook_structure, notebook_file)


def sequential_numbering(path, length=7):
    """Create a new folder with sequential numbering of a specified length."""
    if not os.path.exists(path):
        print(f"The specified path {path} does not exist.")
        return

    # Extract numeric values from folder names and find the highest number
    max_num = 0
    for folder in os.listdir(path):
        if folder.isdigit():
            max_num = max(max_num, int(folder))

    # Create a new folder with the next sequential number
    new_folder_name = str(max_num + 1).zfill(length)
    new_folder_path = os.path.join(path, new_folder_name)
    os.makedirs(new_folder_path)

    print(f"Created new folder: {new_folder_path}")

    # Create a Jupyter notebook inside the new folder
    notebook_name = os.path.join(new_folder_path, f"{new_folder_name}.ipynb")
    create_blank_notebook(notebook_name)
    print(f"Created notebook: {notebook_name}")
