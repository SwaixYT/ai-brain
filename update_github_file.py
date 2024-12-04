import os
from dotenv import load_dotenv
from github import Github
import time

# Load environment variables from the .env file
load_dotenv()

# Access the GitHub token securely
github_token = os.getenv('GITHUB_TOKEN')

if not github_token:
    raise ValueError("GitHub token not found. Make sure it is set in the .env file.")

# Initialize GitHub client
g = Github(github_token)
username = 'SwaixYT'  # Replace with your GitHub username
repo_name = 'ai-brain'  # Replace with your repository name
file_path = 'ai_learning.json'  # Path to the file in the repository

# Get the repository
repo = g.get_user(username).get_repo(repo_name)

# Function to update the file
def update_file():
    try:
        file_content = repo.get_contents(file_path)
        current_content = file_content.decoded_content.decode('utf-8')
        print("Current content fetched successfully.")
        
        # Modify the content (custom logic here)
        updated_content = current_content + "\nNew data added automatically."
        
        # Update the file in the repo
        repo.update_file(
            path=file_path,
            message="Automatic update of the file",
            content=updated_content,
            sha=file_content.sha
        )
        print("File updated successfully.")
    except Exception as e:
        print(f"Error updating the file: {e}")

# Run the update process at defined intervals
while True:
    update_file()
    print("Waiting before next update...")
    time.sleep(3600)  # Run every 1 hour (adjust as needed)
