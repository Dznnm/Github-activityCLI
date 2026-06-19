import sys
import json
import urllib.request
import urllib.error


if len(sys.argv) != 2:
    print("Usage: python github-activity.py <username>")
    sys.exit()
username = sys.argv[1]
url = f"https://api.github.com/users/{username}/events/public"
try:
    urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"Error: User '{username}' not found.")
        sys.exit()
    else:
        print(f"Error: GithHub API returned status code {e.code}.")
        sys.exit()
except urllib.error.URLError:
        print("Error: Unable to connect to GitHub API.")
        sys.exit()
data = urllib.request.urlopen(url).read()
events = json.loads(data)
push_counts = {}
for event in events:
    repo_name = event["repo"]["name"]
    if event["type"] == "PushEvent":
        if repo_name in push_counts:
            push_counts[repo_name] += 1
        else:
            push_counts[repo_name] = 1
    elif event["type"] == "CreateEvent":
        payload = event["payload"]
        print(f"- Created {payload['ref_type']} {payload['ref']} in {repo_name}")
    elif event["type"] == "DeleteEvent":
        payload = event["payload"]
        print(f"- Deleted {payload['ref_type']} {payload['ref']} in {repo_name}")
    elif event["type"] == "ForkEvent":
        print(f"- Forked {repo_name}")
    elif event["type"] == "MemberEvent":
        payload = event["payload"]
        print(f"- Added {payload['member']['login']} to {repo_name}")
    else:
        print(f"- {event['type']} occurred in {repo_name}")
for repo_name, count in push_counts.items():
        word = "time" if count == 1 else "times"
        print(f"- Pushed {count} {word} to {repo_name}")