import os
import subprocess

def get_git_status(folder_path):
    # Change the current working directory to the folder path
    os.chdir(folder_path)

    # Run git status command
    result = subprocess.run(['git', 'status'], capture_output=True, text=True)

    # Return the captured output
    return result.stdout.strip()

def parse_folder_git_status(root_folder):
    # Iterate through each subfolder
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # Check if the path is a directory
        if os.path.isdir(folder_path):
            print(f"Git status for folder: {folder_name}")
            print(get_git_status(folder_path))
            print()

# Provide the root folder path
root_folder_path = '/path/to/root/folder'

# Call the function to parse and display Git status
parse_folder_git_status(root_folder_path)