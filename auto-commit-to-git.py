import os
import subprocess

def git_add(root_folder_path):
    # Change the current working directory to the folder path
    os.chdir(root_folder_path)

    # Run git status to check if folder needs to be updated. 
    status = subprocess.run(['git', 'status'], capture_output=True, text=True)

    print(status.stdout.strip())

    # Run git add command 
    add = subprocess.run(['git', 'add', '.' ], capture_output=True, text=True)

    # Run git commit command with "auto comment"
    commit = subprocess.run(['git', 'commit', '-m','typo fix'], capture_output=True, text=True)
    # Return the captured output

    return print(add.stdout.strip())

def parse_folder_and_add(root_folder_path):
    # Iterate through each subfolder
    for folder_name in os.listdir(root_folder_path):
        folder_path = os.path.join(root_folder_path , folder_name)

        # Check if the path is a directory
        if os.path.isdir(folder_path) and not folder_name.startswith('.'):
            print(f"Git added folders name: {folder_name}")
            git_add(folder_path)


# Provide the root folder path
root_folder_path = '/Users/nathanielewing/Desktop/Code/Current-Projects/'


# Call the function to parse and display Git status
parse_folder_and_add(root_folder_path)