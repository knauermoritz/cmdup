import os
def files():
    current_directory = os.getcwd()

    files_and_folders = os.listdir(current_directory)

    files_and_folders_string = ', '.join(files_and_folders)

    return files_and_folders_string
