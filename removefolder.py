import os

def remove_empty_folders(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                print(f"Removed empty folder: {folder_path}")

# Specify the directory path where you want to remove empty folders
directory_path = "C:\\Users\\Admin\\OneDrive\\Desktop\\PowerPoint"


# Call the function to remove empty folders
remove_empty_folders(directory_path)
