from naming_conventions import sequential_numbering
from dotenv import load_dotenv
import os

load_dotenv()

full_folder_path = os.getenv('FULL_FOLDER_PATH')

if __name__ == '__main__':
    sequential_numbering(full_folder_path)
