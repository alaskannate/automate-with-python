import os
import subprocess



def git_commit_to_github(folder_path, folder_name, files_to_exclude):


    # Change the current working directory to the folder path.
    os.chdir(folder_path)


    # convert excluded files to string.
    excluded_files_str = ", ".join(files_to_exclude)

    # git command varables.
    status = subprocess.run(['git', 'status'], capture_output=True, text=True)

    add = subprocess.run(['git', 'add', '.', '--exclude'] + files_to_exclude, capture_output=True, text=True)
    
    commit = subprocess.run(['git', 'commit', '-m','typo fix'], capture_output=True, text=True)

    upload_to_github = subprocess.run(['git','push','origin','main'], capture_output=True, text=True)

    # Check if there are any changes to commit.
    if 'nothing to commit' not in status.stdout:

            
        add
            
        commit

        upload_to_github
        print(folder_name.capitalize() + " has been pushed to github." + " excluding files inisde of " + excluded_files_str )

    else:
        print(folder_name.capitalize() + " has no changes to commit.")



def parse_folder_for_subfolder_names(root_folder_path):


    # Iterate through each subfolder
    for folder_name in os.listdir(root_folder_path):
        folder_path = os.path.join(root_folder_path , folder_name)

        # Check if the path is a directory

        if os.path.isdir(folder_path):
            git_commit_to_github(folder_path, folder_name , files_to_exclude)
        

# Provide the root folder path
root_folder_path = '/Users/nathanielewing/Desktop/Code/My-Current-Projects/'
# List files to ignore 
files_to_exclude = ['.gitignore']

# Call the function to parse and display Git status
parse_folder_for_subfolder_names(root_folder_path)