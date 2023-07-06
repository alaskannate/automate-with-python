import os
import subprocess

def git_commit_to_github(folder_path):
    # Change the current working directory to the folder path
    os.chdir(folder_path)

    # Run git status command
    status = subprocess.run(['git', 'status'], capture_output=True, text=True)

    # Print the Git status
    print(status.stdout.strip())
    
    add = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)

    # Check if there are any changes to commit
    if 'nothing to commit' not in status.stdout:
        # Run git add command 
        add

        # Print the output
        print(add.stdout.strip())
    else:
        print("No changes to commit.")

    print('\n')

    # Run git commit command with "auto comment"
    commit = subprocess.run(['git', 'commit', '-m','typo fix'], capture_output=True, text=True)

    # upload to gitgub.
    upload_to_github = subprocess.run(['git','push','origin','main'], capture_output=True, text=True)

    # Return the captured output

    return add.stdout.strip()


def parse_folder_for_subfolder_names(root_folder_path):
    # Iterate through each subfolder
    for folder_name in os.listdir(root_folder_path):
        folder_path = os.path.join(root_folder_path , folder_name)

        # Check if the path is a directory
        if os.path.isdir(folder_path) and not folder_name.startswith('.'):
            print (folder_path)
            git_commit_to_github(folder_path)
        

# Provide the root folder path
root_folder_path = '/Users/nathanielewing/Desktop/Code/Current-Projects/'

# Call the function to parse and display Git status
parse_folder_for_subfolder_names(root_folder_path)