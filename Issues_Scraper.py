from github import Github
import json
import os

# Create a Github object
# TODO
g = Github("")

# Specify the list of projects to crawl, and the minimum number of comments
project_list = [
    {"owner": "pingcap", "repo": "ossinsight", "min_comments": 3},
    # {"owner": "zotero", "repo": "zotero", "min_comments": 8},
]

# Define the directory for storing JSON files
dir_name = "github_issues_data"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

# Traverse the project list and crawl data one by one
for project in project_list:
    # Get the repository of the specified project
    repo = g.get_repo(f"{project['owner']}/{project['repo']}")
    
    # Create a directory for storing JSON files
    dir_name_repo = f"{dir_name}/{project['owner']}_{project['repo']}"
    if not os.path.exists(dir_name_repo):
        os.mkdir(dir_name_repo)

    # Get all closed issues and PRs in the repository
    closed_issues = repo.get_issues(state="closed")

    # Traverse all closed issues and their comments
    for issue in closed_issues:
        if not issue.pull_request and issue.comments >= project['min_comments']:  # Only handle issues with enough discussions
            # Process the body of the issue
            # Convert issue.body to string and filter out unparseable characters
            body_str = ""
            if issue.body:
                body_str = str(issue.body.encode('ascii', 'ignore').decode())
            sentences = body_str.split("\r\n\r\n")
            sentences_info = []
            for sentence in sentences:
                sentence_info = {"text": sentence, "_notes": "", "skills": []}
                sentences_info.append(sentence_info)
                
            # Convert datetime data to string
            created_at_str = str(issue.created_at)
            updated_at_str = str(issue.updated_at)
            
            data = {
                "url": issue.html_url,
                "repository": f"{project['owner']}/{project['repo']}",
                "number": issue.number,
                "number_of_comments": issue.comments,
                "title": issue.title,
                "_title_notes": "",
                "title_skills": [],
                "body": sentences_info,
                "_notes": "",
                "body_skills": [],
                "user": {"login": issue.user.login},
                "created_at": created_at_str,
                "updated_at": updated_at_str,
                "comments": []
            }

            # Process the comments of the issue
            issue_comments = issue.get_comments()
            for comment in issue_comments:
                # Convert comment.body to string and filter out unparseable characters
                body_str = ""
                if comment.body:
                    body_str = str(comment.body.encode('ascii', 'ignore').decode())
                comment_sentences = body_str.split("\r\n\r\n")
                comment_sentences_info = []
                for sentence in comment_sentences:
                    sentence_info = {"text": sentence, "_notes": "", "skills": []}
                    comment_sentences_info.append(sentence_info)
                    
                # Convert datetime data to string
                created_at_str = str(comment.created_at)
                updated_at_str = str(comment.updated_at)
                
                comment_data = {
                    "id": comment.id,
                    "user": {"login": comment.user.login},
                    "body": comment_sentences_info,
                    "_notes": "",
                    "comment_skills": [],
                    "created_at": created_at_str,
                    "updated_at": updated_at_str
                }
                data["comments"].append(comment_data)

            # Save all data to a JSON file
            file_name = f"{dir_name_repo}/issue_{issue.number}.json"
            print(project['repo'],file_name)
            with open(file_name, "w", encoding="utf-8") as fp:
                json.dump(data, fp, ensure_ascii=False, indent=4)

            # Pause after crawling an issue to avoid excessive access to the Github API
            # time.sleep(0.1)

# Output a prompt message after crawling all issues
print("Crawling completed!")
