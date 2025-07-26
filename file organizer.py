import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)


        if os.path.isdir(file_path):
            continue

        
        _, ext = os.path.splitext(filename)
        ext = ext[1:].upper()  

        if ext == '':
            ext = 'NO_EXTENSION'

        
        ext_folder = os.path.join(folder_path, ext)
        os.makedirs(ext_folder, exist_ok=True)


        shutil.move(file_path, os.path.join(ext_folder, filename))

    print("Files organized successfully!")


folder_to_organize = input("Enter full path of the folder to organize: ")
organize_folder(folder_to_organize)
