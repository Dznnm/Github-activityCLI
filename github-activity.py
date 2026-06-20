import sys
import json
import urllib.request
import urllib.error


if len(sys.argv) != 2:
    print("Usage: python github-activity.py <username>")
    sys.exit()
username = sys.argv[1]
url = f"https://api.github.com/users/{username}/events"
try:
    response = urllib.request.urlopen(url)
    data = response.read()
    events = json.loads(data)
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"Error: User '{username}' not found.")
        sys.exit()
    else:
        print(f"Error: GitHub API returned status code {e.code}.")
        sys.exit()
except urllib.error.URLError:
    print("Error: Unable to connect to GitHub API.")
    sys.exit()
if not events:
        print(f"No recent activity found for user '{username}'.")
        sys.exit()
for event in events:
    repo_name = event["repo"]["name"]
    if event["type"] == "PushEvent":
        print(f"- Pushed to {repo_name}")
    elif event["type"] == "CreateEvent":
        payload = event["payload"]
        print(f"- Created {payload.get('ref_type')} {payload.get('ref')} in {repo_name}")
    elif event["type"] == "DeleteEvent":
        payload = event["payload"]
        print(f"- Deleted {payload.get('ref_type')} {payload.get('ref')} in {repo_name}")
    elif event["type"] == "ForkEvent":
        print(f"- Forked {repo_name}")
    elif event["type"] == "MemberEvent":
        payload = event["payload"]
        member=payload.get('member', {})
        print(f"- Added {member.get('login')} to {repo_name}")
    else:
        print(f"- {event.get('type')} occurred in {repo_name}")