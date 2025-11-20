import requests
import os
import sys

# --- Configuration ---
TOKEN = os.getenv("TOKEN")  # or paste directly (not recommended)
REPO_OWNER = "GopikrishnaVallepu"
REPO_NAME = "DevSecOps_CICD_Tictactoe_app"
ISSUE_NUMBER = 12  # Could also be PR number
COMMENT_TEXT = "✅ Automated comment: CI/CD pipeline completed successfully."

# --- Function to Post Comment ---
def post_github_comment(owner, repo, issue_number, comment):
    """
    Post a comment to a GitHub issue or PR using REST API.
    """
    url = f"https://api.github.com/repos/gopikrishnavallepu/DevSecOps_CICD_Tictactoe_app/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    print(headers["Authorization"])
    payload = {"body": comment}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"✅ Comment added successfully to issue #{issue_number}")
        print("Response:", response.json()["html_url"])
    else:
        print(f"❌ Failed to add comment. Status: {response.status_code}")
        print(response.text)

# --- Entry point ---
if __name__ == "__main__":
    if not TOKEN:
        print("❌ GITHUB_TOKEN not found. Please export it as an environment variable.")
        sys.exit(1)
    
    post_github_comment(REPO_OWNER, REPO_NAME, ISSUE_NUMBER, COMMENT_TEXT)
