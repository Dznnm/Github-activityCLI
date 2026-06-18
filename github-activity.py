import sys
import json
import urllib.request
import urllib.error

if sys.argv[0] == "github-activity.py":
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events/public"
    urllib.request.urlopen(url)
    response = urllib.request.urlopen(url)
    data = response.read()
    events = json.loads(data)
    for event in events:
        repo_name = event["repo"]["name"]
        if event["type"] == "PushEvent":
            print(f"- Pushed to {repo_name}")
        elif event["type"] == "CreateEvent":
            print(f"- Created {repo_name}")
        elif event["type"] == "DeleteEvent":
            print(f"- Deleted {repo_name}")
        elif event["type"] == "ForkEvent":
            print(f"- Forked {repo_name}")
        elif event["type"] == "MemberEvent":
            print(f"- Added a member to {repo_name}")
        else:
            print(f"- {event['type']} in {repo_name}")