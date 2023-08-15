
import os
import subprocess

def log_error(error_message, root_folder_path):
    with open(os.path.join(root_folder_path, 'error_ledger.txt'), 'a') as file:
        file.write(error_message + '\n')

def check_git_status(folder_path):
    status = subprocess.run(['git', 'status'], capture_output=True, text=True)
    if status.returncode != 0:
        log_error(f"An error occurred while checking status: {{status.stderr}}", root_folder_path)
        return False
    return True

def add_files_to_git(folder_path, files_to_exclude):
    all_files = os.listdir(folder_path)
    files_to_add = [file for file in all_files if file not in files_to_exclude]
    for file in files_to_add:
        add_command = subprocess.run(['git', 'add', file], capture_output=True, text=True)
        if add_command.returncode != 0:
            log_error(f"An error occurred while adding {{file}}: {{add_command.stderr}}", root_folder_path)
            return False
    return files_to_add

def commit_changes(commit_message):
    commit = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
    if commit.returncode != 0:
        log_error(f"An error occurred while committing: {{commit.stderr}}", root_folder_path)
        return False
    return True

def push_to_github():
    push_command = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
    if push_command.returncode != 0:
        log_error(f"An error occurred while pushing to GitHub: {{push_command.stderr}}", root_folder_path)
        return False
    return True

def determine_commit_message(files_to_add):
    if any(file.endswith('.css') for file in files_to_add):
        return 'style changed'
    elif any(file.endswith(('.js', '.py')) for file in files_to_add):
        return 'functionality changed'
    else:
        return 'updated minor typos'

def git_commit_to_github(folder_path, folder_name, files_to_exclude):
    os.chdir(folder_path)
    excluded_files_str = ", ".join(files_to_exclude)

    # Check git status
    if not check_git_status(folder_path):
        return

    # Add files to git
    files_to_add = add_files_to_git(folder_path, files_to_exclude)
    if files_to_add is False:
        return

    # Determine commit message
    commit_message = determine_commit_message(files_to_add)

    # Commit changes
    if not commit_changes(commit_message):
        return

    # Push to GitHub
    if not push_to_github():
        return

    print(folder_name.capitalize() + " has been pushed to github. excluding files inside of " + excluded_files_str)
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
files_to_exclude = ['.gitignore', 'error_ledger.txt']

# Call the function to parse and display Git status
parse_folder_for_subfolder_names(root_folder_path)