import os
import subprocess

# Provide the root folder path
root_folder_path = '/Users/nathanielewing/Desktop/Code/My-Current-Projects/'
# List files to ignore 
files_to_exclude = ['.gitignore', '.env']

    
def parse_through_subfolders(root_folder_path, files_to_exclude):
    # Iterate through each subfolder, create a new path for the iterated folder.
    for folder_name in os.listdir(root_folder_path):
        folder_path = os.path.join(root_folder_path, folder_name)

        # Check if the path is a directory
        if os.path.isdir(folder_path):
            git_commit_to_github(folder_path, folder_name, files_to_exclude)



def git_add(files_to_exclude, folder_path):
    # Create or append to .gitignore file
    with open(os.path.join(folder_path, '.gitignore'), 'a') as gitignore_file:
        gitignore_file.write('\n'.join(files_to_exclude) + '\n')

    # Run the git add command
    subprocess.run(['git', 'add', '.'], capture_output=True, text=True)


def git_commit(commit_message):
    result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
    return "nothing to commit, working tree clean" not in result.stdout


def git_push_to_github():
    subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)



def git_commit_to_github(folder_path, folder_name, files_to_exclude):
    # Change the current working directory to the parsed folder path.
    os.chdir(folder_path)

    # Add files excluding the specified ones
    git_add(files_to_exclude, folder_path)

    # Define the commit message
    commit_message = folder_name.capitalize() + " changes."

    # Commit changes
    commit_made = git_commit(commit_message)

    if commit_made:
        # Push changes to GitHub
        git_push_to_github()

        # Print success message
        excluded_files_str = ', '.join(files_to_exclude)
        print(folder_name.capitalize() + " has been pushed to GitHub, excluding files inside of " + excluded_files_str)
    else:
        print(folder_name.capitalize() + " has no changes to commit.")


parse_through_subfolders(root_folder_path, files_to_exclude)