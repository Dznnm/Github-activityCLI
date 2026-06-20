# GitHub Activity CLI

A simple command-line application that fetches and displays a GitHub user's recent public activity using the GitHub API.

This project was built as part of the roadmap.sh backend projects.

## Project URL

https://roadmap.sh/projects/github-user-activity

## Features

* Accepts a GitHub username as a command-line argument
* Fetches recent public activity from the GitHub API
* Displays activity in a human-readable format
* Handles invalid usernames
* Handles API connection failures
* Supports multiple GitHub event types

Supported event types:

* PushEvent
* CreateEvent
* DeleteEvent
* ForkEvent
* MemberEvent

Unknown event types are displayed using a generic fallback message.

---

## Usage

Run the application from the command line:

```bash
python github-activity.py <username>
```

Example:

```bash
python github-activity.py dznnm
```

---

## Example Output

```text
- Pushed to Dznnm/Github-activityCLI
- Created branch main in Dznnm/Github-activityCLI
- Deleted branch old-feature in Dznnm/Github-activityCLI
- Forked Introduceirfan/Database_app
- Added username to repository-name
```

---

## Error Handling

### Invalid Username

```text
Error: User 'unknownuser' not found.
```

### API Connection Failure

```text
Error: Unable to connect to GitHub API.
```

### Other GitHub API Errors

```text
Error: GitHub API returned status code XXX.
```

---

## Technical Notes

This project uses:

* Python Standard Library only
* `urllib.request` for HTTP requests
* `urllib.error` for error handling
* `json` for parsing API responses

No external libraries or frameworks were used.

---

## Note About Push Events

The original project example shows output similar to:

```text
- Pushed 3 commits to owner/repository
```

During development, the GitHub Events API endpoint used by this project did not consistently provide commit information in the `payload` section of returned `PushEvent` objects.

Example payload received:

```json
{
  "repository_id": 1272269030,
  "push_id": 35754776794,
  "ref": "refs/heads/main",
  "head": "32553f9dbea7d4a51456318af43a9533d86926cd",
  "before": "ad2fe0a8ac89cd0c8f9322b89d399492c7f4b8a5"
}
```

Since commit details were not available in the returned payload, the application reports PushEvents as:

```
- Pushed to repository-name
```

instead of displaying a commit count.

This ensures that the output accurately reflects the data returned by the API rather than making assumptions about the number of commits.

---

## Learning Objectives

This project provided practice with:

* Command-line arguments (`sys.argv`)
* HTTP requests
* Working with APIs
* JSON parsing
* Dictionary and nested dictionary access
* Error handling with exceptions
* Processing and displaying structured data

```
```
